"""Offline contract tests for Sign in with ChatGPT credentials."""

from __future__ import annotations

import json
import stat
import time

import httpx
import pytest

from deerflow import siwc_auth


def _credential(**overrides):
    value = {
        "client_id": "oaiapp_test",
        "subject": "user-1",
        "issuer": "https://auth.openai.com",
        "ext_agent_host_id": "urn:uuid:00000000-0000-4000-8000-000000000001",
        "access_token": "access-old",
        "refresh_token": "refresh-old",
        "id_token": "id-token",
        "scopes": ["openid", "offline_access", "resource.invoke", "chatgpt.tokens.use.direct"],
        "expires_in": 3600,
        "saved_at": time.time(),
    }
    return {**value, **overrides}


def test_credential_path_follows_runtime_home_without_loading_config(tmp_path, monkeypatch):
    monkeypatch.delenv("DEER_FLOW_CHATGPT_AUTH_PATH", raising=False)
    monkeypatch.delenv("DEER_FLOW_PROJECT_ROOT", raising=False)
    monkeypatch.delenv("DEER_FLOW_HOME", raising=False)
    monkeypatch.chdir(tmp_path)
    assert siwc_auth.credential_path() == tmp_path / ".deer-flow" / "chatgpt-auth.json"

    monkeypatch.setenv("DEER_FLOW_HOME", str(tmp_path / "state"))
    assert siwc_auth.credential_path() == tmp_path / "state" / "chatgpt-auth.json"


def test_save_credentials_are_atomic_and_owner_only(tmp_path):
    path = tmp_path / "auth" / "chatgpt-auth.json"
    siwc_auth.save_credentials(path, _credential())

    assert siwc_auth.load_credentials(path)["client_id"] == "oaiapp_test"
    assert stat.S_IMODE(path.stat().st_mode) == 0o600
    assert not list(path.parent.glob("*.tmp"))


def test_codex_cli_auth_is_not_accepted_as_siwc_auth(tmp_path):
    path = tmp_path / "auth.json"
    path.write_text(json.dumps({"tokens": {"access_token": "codex-token"}}), encoding="utf-8")

    with pytest.raises(siwc_auth.ChatGPTAuthError, match="Sign in with ChatGPT"):
        siwc_auth.load_credentials(path)


def test_refresh_rotates_tokens_and_preserves_registration(tmp_path):
    path = tmp_path / "auth.json"
    siwc_auth.save_credentials(path, _credential(saved_at=1))
    requests = []

    def respond(request):
        requests.append(request)
        return httpx.Response(
            200,
            json={
                "access_token": "access-new",
                "refresh_token": "refresh-new",
                "expires_in": 3600,
                "scope": "openid offline_access resource.invoke chatgpt.tokens.use.direct",
                "token_type": "Bearer",
            },
        )

    with httpx.Client(transport=httpx.MockTransport(respond)) as client:
        assert siwc_auth.get_access_token(path, client=client) == "access-new"

    saved = siwc_auth.load_credentials(path)
    assert saved["refresh_token"] == "refresh-new"
    assert saved["client_id"] == "oaiapp_test"
    assert saved["ext_agent_host_id"] == _credential()["ext_agent_host_id"]
    assert b"grant_type=refresh_token" in requests[0].content
    assert b"client_id=oaiapp_test" in requests[0].content
    assert b"resource=https%3A%2F%2Fapi.openai.com%2Fv1" in requests[0].content
    assert b"scope=" not in requests[0].content


def test_refresh_without_plan_scope_does_not_replace_saved_credentials(tmp_path):
    path = tmp_path / "auth.json"
    original = _credential(saved_at=1)
    siwc_auth.save_credentials(path, original)

    with httpx.Client(
        transport=httpx.MockTransport(
            lambda _: httpx.Response(
                200,
                json={
                    "access_token": "access-new",
                    "refresh_token": "refresh-new",
                    "expires_in": 3600,
                    "scope": "openid profile",
                },
            )
        )
    ) as client:
        with pytest.raises(siwc_auth.ChatGPTAuthError, match="permission"):
            siwc_auth.get_access_token(path, client=client)

    assert siwc_auth.load_credentials(path)["refresh_token"] == original["refresh_token"]


def test_valid_token_needs_no_network(tmp_path):
    path = tmp_path / "auth.json"
    siwc_auth.save_credentials(path, _credential())
    assert siwc_auth.get_access_token(path) == "access-old"
