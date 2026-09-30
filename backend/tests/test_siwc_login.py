"""Local loopback login parameters for ChatGPT plan access."""

from __future__ import annotations

from urllib.parse import parse_qs, urlparse

from scripts.chatgpt_login import authorization_url, resolve_callback_client_id


def test_first_authorization_uses_dynamic_registration_and_pkce():
    url = authorization_url(
        client_id="dynamic_agent_client",
        host_id="urn:uuid:00000000-0000-4000-8000-000000000001",
        redirect_uri="http://127.0.0.1:12345/auth/callback",
        state="state-1",
        nonce="nonce-1",
        verifier="verifier-1",
    )
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    assert parsed.scheme == "https" and parsed.netloc == "auth.openai.com"
    assert query["client_id"] == ["dynamic_agent_client"]
    assert query["agent_name_hint"] == ["DeerFlow"]
    assert query["ext_agent_host_id"] == ["urn:uuid:00000000-0000-4000-8000-000000000001"]
    assert query["resource"] == ["https://api.openai.com/v1"]
    assert "chatgpt.tokens.use.direct" in query["scope"][0].split()
    assert query["code_challenge_method"] == ["S256"]
    assert query["redirect_uri"] == ["http://127.0.0.1:12345/auth/callback"]


def test_registration_requires_issued_client_id():
    assert resolve_callback_client_id("dynamic_agent_client", "oaiapp_123") == "oaiapp_123"


def test_returning_client_id_cannot_be_replaced():
    try:
        resolve_callback_client_id("oaiapp_old", "oaiapp_other")
    except ValueError as exc:
        assert "client ID" in str(exc)
    else:
        raise AssertionError("unexpected client replacement")


def test_login_saves_issued_client_and_validated_identity(tmp_path, monkeypatch):
    from unittest.mock import patch

    import httpx

    from deerflow.siwc_auth import load_credentials
    from scripts import chatgpt_login

    path = tmp_path / "chatgpt-auth.json"
    monkeypatch.setattr(chatgpt_login.webbrowser, "open", lambda _url: True)
    monkeypatch.setattr(chatgpt_login, "_wait_for_callback", lambda _server, _state, **_kwargs: {"code": "code-1", "client_id": "oaiapp_issued"})

    async def verify(_token, _client_id, _nonce):
        return {"sub": "user-1", "email": "user@example.com"}

    monkeypatch.setattr(chatgpt_login, "_verify_id_token", verify)

    def respond(request):
        assert request.url.path.endswith("/oauth/token")
        assert b"client_id=oaiapp_issued" in request.content
        assert b"code_verifier=" in request.content
        return httpx.Response(
            200,
            json={
                "id_token": "id-token",
                "access_token": "access-token",
                "refresh_token": "refresh-token",
                "token_type": "Bearer",
                "scope": "openid offline_access resource.invoke chatgpt.tokens.use.direct",
                "expires_in": 3600,
            },
        )

    real_client = httpx.Client
    with real_client(transport=httpx.MockTransport(respond)) as client:

        class SharedClient:
            def __init__(self, **_kwargs):
                pass

            def __enter__(self):
                return client

            def __exit__(self, *_args):
                return None

        with patch.object(chatgpt_login.httpx, "Client", SharedClient):
            chatgpt_login.login(path)

    saved = load_credentials(path)
    assert saved["client_id"] == "oaiapp_issued"
    assert saved["subject"] == "user-1"
    assert saved["ext_agent_host_id"].startswith("urn:uuid:")


def test_oidc_verifier_loads_without_gateway_package():
    from scripts.chatgpt_login import _load_oidc_verifier

    verifier = _load_oidc_verifier()
    assert verifier.OIDCService.__module__ == "_deerflow_chatgpt_oidc"
    assert verifier.OIDCError.__module__ == "_deerflow_chatgpt_oidc"


def test_explicit_browser_opens_login_outside_default_browser(monkeypatch):
    from unittest.mock import Mock

    from scripts import chatgpt_login

    controller = Mock()
    controller.open.return_value = True
    get_browser = Mock(return_value=controller)
    monkeypatch.setattr(chatgpt_login.webbrowser, "get", get_browser)
    monkeypatch.setattr(chatgpt_login.webbrowser, "open", Mock(side_effect=AssertionError("default browser must not open")))

    chatgpt_login._open_login_browser("https://auth.openai.com/example", browser="firefox")

    get_browser.assert_called_once_with("firefox")
    controller.open.assert_called_once_with("https://auth.openai.com/example")


def test_browser_launch_failure_keeps_manual_login_available(monkeypatch, capsys):
    from unittest.mock import Mock

    from scripts import chatgpt_login

    monkeypatch.setattr(chatgpt_login.webbrowser, "get", Mock(side_effect=chatgpt_login.webbrowser.Error("not installed")))
    chatgpt_login._open_login_browser("https://auth.openai.com/example", browser="missing")
    assert "copy the URL" in capsys.readouterr().out


def test_callback_timeout_explains_browser_recovery(monkeypatch):
    from unittest.mock import Mock

    import pytest

    from scripts import chatgpt_login

    server = Mock()
    monkeypatch.setattr(chatgpt_login.time, "monotonic", Mock(side_effect=[0, 0, 601]))
    with pytest.raises(chatgpt_login.ChatGPTAuthError, match="system browser"):
        chatgpt_login._wait_for_callback(server, "expected-state")
    server.handle_request.assert_called_once()


def test_id_token_verifies_rsa_signature_and_rejects_wrong_nonce(monkeypatch):
    import asyncio
    import json
    import time

    import httpx
    import jwt
    import pytest
    from cryptography.hazmat.primitives.asymmetric import rsa

    from scripts import chatgpt_login

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    jwk = {**json.loads(jwt.algorithms.RSAAlgorithm.to_jwk(key.public_key())), "kid": "test-key", "alg": "RS256"}
    claims = {"iss": chatgpt_login.ISSUER, "sub": "test-user", "aud": "oaiapp_test", "exp": int(time.time()) + 300, "nonce": "expected-nonce"}
    token = jwt.encode(claims, key, algorithm="RS256", headers={"kid": "test-key"})

    def respond(request):
        if request.url.path == "/.well-known/openid-configuration":
            return httpx.Response(200, json={"issuer": chatgpt_login.ISSUER, "authorization_endpoint": chatgpt_login.AUTHORIZATION_URL, "token_endpoint": chatgpt_login.TOKEN_URL, "jwks_uri": f"{chatgpt_login.ISSUER}/jwks"})
        assert request.url.path == "/jwks"
        return httpx.Response(200, json={"keys": [jwk]})

    real_client = httpx.AsyncClient
    monkeypatch.setattr(httpx, "AsyncClient", lambda **kwargs: real_client(transport=httpx.MockTransport(respond), **kwargs))
    verified = asyncio.run(chatgpt_login._verify_id_token(token, "oaiapp_test", "expected-nonce"))
    assert verified["sub"] == "test-user"
    with pytest.raises(chatgpt_login.ChatGPTAuthError, match="validate ChatGPT identity"):
        asyncio.run(chatgpt_login._verify_id_token(token, "oaiapp_test", "wrong-nonce"))
