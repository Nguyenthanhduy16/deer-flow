"""Credentials for the official Sign in with ChatGPT plan-usage flow.

The operator signs in on the host using ``scripts/chatgpt_login.py``. The
Gateway reads one protected credential file from its runtime home and renews
the rotating OAuth session before inference. This is intentionally separate
from Codex CLI's auth.json, whose tokens belong to another OAuth client.
"""

from __future__ import annotations

import json
import os
import tempfile
import time
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import httpx

API_RESOURCE = "https://api.openai.com/v1"
RESPONSES_URL = f"{API_RESOURCE}/responses"
MODELS_URL = f"{API_RESOURCE}/models"
TOKEN_URL = "https://auth.openai.com/api/accounts/oauth/token"
PLAN_SCOPE = "chatgpt.tokens.use.direct"
_REFRESH_SKEW_SECONDS = 90


class ChatGPTAuthError(RuntimeError):
    """A safe, actionable credential error (never contains token material)."""


def credential_path() -> Path:
    configured = os.getenv("DEER_FLOW_CHATGPT_AUTH_PATH")
    if configured:
        return Path(configured).expanduser()
    runtime_home = os.getenv("DEER_FLOW_HOME")
    if runtime_home:
        return Path(runtime_home).resolve() / "chatgpt-auth.json"
    project_root = os.getenv("DEER_FLOW_PROJECT_ROOT")
    return (Path(project_root).resolve() if project_root else Path.cwd().resolve()) / ".deer-flow" / "chatgpt-auth.json"


def _validate(data: Any) -> dict[str, Any]:
    if not isinstance(data, dict) or not all(isinstance(data.get(key), str) and data[key] for key in ("client_id", "subject", "access_token", "refresh_token", "ext_agent_host_id")):
        raise ChatGPTAuthError("Sign in with ChatGPT credentials are missing or invalid. Run `make chatgpt-login`.")
    if data["client_id"] == "dynamic_agent_client":
        raise ChatGPTAuthError("Sign in with ChatGPT registration is incomplete. Run `make chatgpt-login`.")
    scopes = data.get("scopes")
    if not isinstance(scopes, list) or PLAN_SCOPE not in scopes:
        raise ChatGPTAuthError("ChatGPT plan permission was not granted. Run `make chatgpt-login` and approve plan usage.")
    if not isinstance(data.get("saved_at"), (int, float)) or not isinstance(data.get("expires_in"), (int, float)):
        raise ChatGPTAuthError("Sign in with ChatGPT credential expiry is missing. Run `make chatgpt-login`.")
    return data


def load_credentials(path: Path | None = None) -> dict[str, Any]:
    path = path or credential_path()
    try:
        if path.is_symlink():
            raise ChatGPTAuthError("Sign in with ChatGPT credential path must be a regular file.")
        with path.open(encoding="utf-8") as stream:
            data = json.load(stream)
    except (OSError, ValueError) as exc:
        raise ChatGPTAuthError("Sign in with ChatGPT credentials are unavailable. Run `make chatgpt-login`.") from exc
    return _validate(data)


def write_secret_json(path: Path, data: dict[str, Any]) -> None:
    """Replace one credential record atomically with owner-only permissions."""
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.is_symlink():
        raise ChatGPTAuthError("Sign in with ChatGPT credential path must be a regular file.")
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.", suffix=".tmp", delete=False) as stream:
            temp_name = stream.name
            os.chmod(temp_name, 0o600)
            json.dump(data, stream, ensure_ascii=False, separators=(",", ":"))
            stream.flush()
            os.fsync(stream.fileno())
        # A root-running Docker Gateway may refresh a host-owned bind mount.
        # Keep the original owner so a later host-side login can still read it.
        if path.exists() and hasattr(os, "geteuid") and os.geteuid() == 0:
            original = path.stat()
            os.chown(temp_name, original.st_uid, original.st_gid)
        os.replace(temp_name, path)
        os.chmod(path, 0o600)
    finally:
        if temp_name and os.path.exists(temp_name):
            os.unlink(temp_name)


@contextmanager
def _credential_lock(path: Path) -> Iterator[None]:
    """Serialize refreshes across Gateway workers sharing a runtime volume."""
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    lock_path = path.with_name(path.name + ".lock")
    fd = os.open(lock_path, os.O_CREAT | os.O_RDWR, 0o600)
    try:
        if os.name == "nt":
            import msvcrt

            os.write(fd, b" ")
            os.lseek(fd, 0, os.SEEK_SET)
            msvcrt.locking(fd, msvcrt.LK_LOCK, 1)
        else:
            import fcntl

            fcntl.flock(fd, fcntl.LOCK_EX)
        try:
            yield
        finally:
            if os.name == "nt":
                os.lseek(fd, 0, os.SEEK_SET)
                msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(fd, fcntl.LOCK_UN)
    finally:
        os.close(fd)


def save_credentials(path: Path, data: dict[str, Any]) -> None:
    _validate(data)
    with _credential_lock(path):
        write_secret_json(path, data)


def get_access_token(path: Path | None = None, *, client: httpx.Client | None = None) -> str:
    """Return a usable access token, refreshing and persisting a rotated grant."""
    path = path or credential_path()
    with _credential_lock(path):
        data = load_credentials(path)
        if data["saved_at"] + data["expires_in"] > time.time() + _REFRESH_SKEW_SECONDS:
            return data["access_token"]

        owns_client = client is None
        client = client or httpx.Client(timeout=15.0)
        try:
            response = client.post(
                TOKEN_URL,
                data={
                    "grant_type": "refresh_token",
                    "client_id": data["client_id"],
                    "refresh_token": data["refresh_token"],
                    "resource": API_RESOURCE,
                },
            )
            response.raise_for_status()
            refreshed = response.json()
        except (httpx.HTTPError, ValueError) as exc:
            raise ChatGPTAuthError("Could not refresh ChatGPT plan access. Reconnect with `make chatgpt-login`.") from exc
        finally:
            if owns_client:
                client.close()

        if not isinstance(refreshed, dict) or not all(isinstance(refreshed.get(key), str) and refreshed[key] for key in ("access_token", "refresh_token")):
            raise ChatGPTAuthError("ChatGPT token refresh returned incomplete credentials. Reconnect with `make chatgpt-login`.")
        if refreshed.get("token_type", "Bearer").lower() != "bearer":
            raise ChatGPTAuthError("ChatGPT token refresh returned an unsupported token type.")
        scopes = refreshed.get("scope")
        if scopes is not None and (not isinstance(scopes, str) or PLAN_SCOPE not in scopes.split()):
            raise ChatGPTAuthError("ChatGPT plan permission is no longer active. Reconnect with `make chatgpt-login`.")
        expires_in = refreshed.get("expires_in")
        if not isinstance(expires_in, (int, float)) or expires_in <= 0:
            raise ChatGPTAuthError("ChatGPT token refresh returned an invalid expiry.")

        updated = {
            **data,
            "access_token": refreshed["access_token"],
            "refresh_token": refreshed["refresh_token"],
            "expires_in": expires_in,
            "saved_at": time.time(),
            "scopes": scopes.split() if scopes is not None else data["scopes"],
        }
        if isinstance(refreshed.get("id_token"), str) and refreshed["id_token"]:
            updated["id_token"] = refreshed["id_token"]
        write_secret_json(path, updated)
        return updated["access_token"]
