"""Connect a local DeerFlow Gateway to a ChatGPT Plus/Pro plan.

Run on the computer with the browser: ``make chatgpt-login`` from the repo root.
The listener binds only 127.0.0.1; the Gateway never receives the OAuth code.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import hashlib
import importlib.util
import json
import secrets
import sys
import time
import uuid
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "packages" / "harness"))

from deerflow.siwc_auth import (  # noqa: E402
    API_RESOURCE,
    MODELS_URL,
    PLAN_SCOPE,
    TOKEN_URL,
    ChatGPTAuthError,
    credential_path,
    get_access_token,
    load_credentials,
    save_credentials,
    write_secret_json,
)

AUTHORIZATION_URL = "https://auth.openai.com/api/accounts/authorize"
ISSUER = "https://auth.openai.com"
SCOPES = "openid profile email offline_access resource.invoke chatgpt.tokens.use.direct"
CALLBACK_PATH = "/auth/callback"
LOGIN_TIMEOUT_SECONDS = 600


def authorization_url(*, client_id: str, host_id: str, redirect_uri: str, state: str, nonce: str, verifier: str) -> str:
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode("ascii")).digest()).rstrip(b"=").decode("ascii")
    params = {
        "client_id": client_id,
        "ext_agent_host_id": host_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": SCOPES,
        "resource": API_RESOURCE,
        "state": state,
        "nonce": nonce,
        "code_challenge_method": "S256",
        "code_challenge": challenge,
    }
    if client_id == "dynamic_agent_client":
        params["agent_name_hint"] = "DeerFlow"
    return f"{AUTHORIZATION_URL}?{urlencode(params)}"


def resolve_callback_client_id(requested: str, returned: str | None) -> str:
    if requested == "dynamic_agent_client":
        if not returned or returned == requested:
            raise ValueError("Registration callback did not include an issued client ID")
        return returned
    if returned and returned != requested:
        raise ValueError("Authorization callback returned a different client ID")
    return requested


def _host_id(path: Path) -> str:
    host_path = path.with_name("chatgpt-host.json")
    if host_path.exists():
        try:
            value = json.loads(host_path.read_text(encoding="utf-8"))["ext_agent_host_id"]
        except (OSError, ValueError, KeyError) as exc:
            raise ChatGPTAuthError("ChatGPT host ID file is invalid; restore it before signing in again.") from exc
        if not isinstance(value, str) or not value.startswith("urn:uuid:"):
            raise ChatGPTAuthError("ChatGPT host ID file is invalid; restore it before signing in again.")
        return value
    value = f"urn:uuid:{uuid.uuid4()}"
    write_secret_json(host_path, {"ext_agent_host_id": value})
    return value


def _wait_for_callback(server: HTTPServer, expected_state: str, timeout_seconds: float = LOGIN_TIMEOUT_SECONDS) -> dict[str, str]:
    callback: dict[str, str] = {}

    class CallbackHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler interface
            parsed = urlparse(self.path)
            params = parse_qs(parsed.query)
            if parsed.path != CALLBACK_PATH or params.get("state") != [expected_state]:
                self.send_error(400, "Invalid OAuth callback")
                return
            for key in ("code", "client_id", "error"):
                if len(params.get(key, [])) == 1:
                    callback[key] = params[key][0]
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"DeerFlow sign-in received. You may close this tab.")

        def log_message(self, format: str, *args: object) -> None:
            # The request URL carries an authorization code and must not be logged.
            return

    # The server is constructed before the browser opens; assign its handler
    # here so the fresh state stays private to this one authorization attempt.
    server.RequestHandlerClass = CallbackHandler
    server.timeout = 1.0
    deadline = time.monotonic() + timeout_seconds
    while not callback and time.monotonic() < deadline:
        server.handle_request()
    if not callback:
        raise ChatGPTAuthError("ChatGPT sign-in timed out. Start a fresh login and open its URL in a system browser such as Firefox or Chrome. Complete any browser verification yourself and keep this terminal open until sign-in finishes.")
    return callback


def _load_oidc_verifier():
    """Use the Gateway's verifier without importing the full auth package."""
    module_name = "_deerflow_chatgpt_oidc"
    if module_name not in sys.modules:
        module_path = Path(__file__).resolve().parents[1] / "app" / "gateway" / "auth" / "oidc.py"
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        if spec is None or spec.loader is None:
            raise ChatGPTAuthError("Could not load the ChatGPT identity verifier.")
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        try:
            spec.loader.exec_module(module)
        except Exception:
            del sys.modules[module_name]
            raise
    return sys.modules[module_name]


async def _verify_id_token(id_token: str, client_id: str, nonce: str) -> dict:
    # Reuse the Gateway's tested JWKS, signature, audience, issuer, expiry, and
    # nonce validation rather than trusting claims from the browser callback.
    verifier_module = _load_oidc_verifier()
    OIDCError = verifier_module.OIDCError
    OIDCService = verifier_module.OIDCService
    service = OIDCService()
    try:
        metadata = await service.discover(ISSUER)
        if metadata.issuer != ISSUER:
            raise ChatGPTAuthError("OpenAI returned an unexpected token issuer.")
        return await service.validate_id_token(metadata, client_id, id_token, nonce=nonce)
    except OIDCError as exc:
        raise ChatGPTAuthError("Could not validate ChatGPT identity. Start a fresh sign-in.") from exc
    finally:
        await service.close()


def _open_login_browser(url: str, *, browser: str | None = None) -> None:
    try:
        opened = webbrowser.get(browser).open(url) if browser else webbrowser.open(url)
    except (webbrowser.Error, OSError):
        opened = False
    if not opened:
        print("Could not open the browser; copy the URL above into Firefox or Chrome on this computer.", flush=True)


def login(path: Path, *, browser: str | None = None, no_browser: bool = False, timeout_seconds: int = LOGIN_TIMEOUT_SECONDS) -> None:
    host_id = _host_id(path)
    try:
        existing = load_credentials(path)
    except ChatGPTAuthError:
        existing = None
    if existing and existing["ext_agent_host_id"] != host_id:
        raise ChatGPTAuthError("This credential belongs to a different DeerFlow host. Reconnect it on this host.")
    requested_client_id = existing["client_id"] if existing else "dynamic_agent_client"
    verifier = secrets.token_urlsafe(64)
    state = secrets.token_urlsafe(32)
    nonce = secrets.token_urlsafe(32)

    class _Placeholder(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            self.send_error(503)

        def log_message(self, format: str, *args: object) -> None:
            return

    with HTTPServer(("127.0.0.1", 0), _Placeholder) as server:
        redirect_uri = f"http://127.0.0.1:{server.server_port}{CALLBACK_PATH}"
        url = authorization_url(client_id=requested_client_id, host_id=host_id, redirect_uri=redirect_uri, state=state, nonce=nonce, verifier=verifier)
        print("Continue with ChatGPT in a system browser on this computer:", flush=True)
        print(url, flush=True)
        print(f"Waiting up to {timeout_seconds} seconds. Keep this terminal open until sign-in finishes.", flush=True)
        print("If an embedded browser gets stuck on security verification, copy this URL into Firefox or Chrome and complete verification yourself.", flush=True)
        if not no_browser:
            _open_login_browser(url, browser=browser)
        callback = _wait_for_callback(server, state, timeout_seconds=timeout_seconds)

    if callback.get("error"):
        raise ChatGPTAuthError("ChatGPT sign-in was declined or could not be completed.")
    code = callback.get("code")
    if not code:
        raise ChatGPTAuthError("ChatGPT authorization callback contained no code.")
    client_id = resolve_callback_client_id(requested_client_id, callback.get("client_id"))
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.post(
                TOKEN_URL,
                data={
                    "grant_type": "authorization_code",
                    "client_id": client_id,
                    "code": code,
                    "code_verifier": verifier,
                    "redirect_uri": redirect_uri,
                    "resource": API_RESOURCE,
                },
            )
            response.raise_for_status()
            tokens = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise ChatGPTAuthError("ChatGPT code exchange failed. Start a fresh sign-in.") from exc
    if not isinstance(tokens, dict) or not all(isinstance(tokens.get(key), str) and tokens[key] for key in ("id_token", "access_token", "refresh_token")):
        raise ChatGPTAuthError("ChatGPT code exchange returned incomplete credentials.")
    if tokens.get("token_type", "Bearer").lower() != "bearer":
        raise ChatGPTAuthError("ChatGPT code exchange returned an unsupported token type.")
    scopes = tokens.get("scope", "").split()
    if PLAN_SCOPE not in scopes:
        raise ChatGPTAuthError("ChatGPT plan permission was not granted. Reconnect and approve plan usage.")
    expires_in = tokens.get("expires_in")
    if not isinstance(expires_in, (int, float)) or expires_in <= 0:
        raise ChatGPTAuthError("ChatGPT code exchange returned an invalid expiry.")
    claims = asyncio.run(_verify_id_token(tokens["id_token"], client_id, nonce))
    if existing and claims["sub"] != existing["subject"]:
        raise ChatGPTAuthError("A different ChatGPT account was selected for this registration.")

    save_credentials(
        path,
        {
            "client_id": client_id,
            "subject": claims["sub"],
            "issuer": ISSUER,
            "email": claims.get("email", ""),
            "ext_agent_host_id": host_id,
            "id_token": tokens["id_token"],
            "access_token": tokens["access_token"],
            "refresh_token": tokens["refresh_token"],
            "token_type": "Bearer",
            "scopes": scopes,
            "expires_in": expires_in,
            "saved_at": time.time(),
        },
    )
    print(f"Connected ChatGPT account: {claims.get('email') or claims['sub']}")
    print(f"Credential file: {path}")


def models(path: Path) -> None:
    token = get_access_token(path)
    try:
        with httpx.Client(timeout=15.0) as client:
            response = client.get(MODELS_URL, headers={"Authorization": f"Bearer {token}"})
            response.raise_for_status()
            data = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise ChatGPTAuthError("Could not load models available to this ChatGPT account.") from exc
    if not isinstance(data, dict) or not isinstance(data.get("models"), list):
        raise ChatGPTAuthError("ChatGPT returned an invalid model catalog.")
    for item in data["models"]:
        if isinstance(item, dict) and item.get("visibility") == "list" and isinstance(item.get("slug"), str):
            print(f"{item['slug']}\t{item.get('display_name') or item['slug']}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Connect DeerFlow to your ChatGPT plan")
    parser.add_argument("command", choices=("login", "status", "models"), nargs="?", default="login")
    parser.add_argument("--auth-path", type=Path, default=credential_path())
    parser.add_argument("--browser", help="Browser name supported by Python, e.g. firefox or chrome (login only)")
    parser.add_argument("--no-browser", action="store_true", help="Print the login URL without opening a browser")
    parser.add_argument("--timeout", type=int, default=LOGIN_TIMEOUT_SECONDS, help="Seconds to wait for login (default: 600)")
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be greater than zero")
    try:
        if args.command == "login":
            login(args.auth_path, browser=args.browser, no_browser=args.no_browser, timeout_seconds=args.timeout)
        elif args.command == "status":
            credential = load_credentials(args.auth_path)
            print(f"Connected ChatGPT account: {credential.get('email') or credential['subject']}")
            print(f"Credential file: {args.auth_path}")
        else:
            models(args.auth_path)
    except KeyboardInterrupt:
        parser.exit(130, "ChatGPT sign-in cancelled. Start a fresh login to try again.\n")
    except (ChatGPTAuthError, ValueError) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
