"""Official ChatGPT plan provider request contract."""

from __future__ import annotations

from unittest.mock import patch

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage

from deerflow.models.openai_codex_provider import ChatGPTPlanChatModel


def _model():
    with patch("deerflow.models.openai_codex_provider.load_siwc_credentials", return_value={"client_id": "oaiapp_test"}):
        return ChatGPTPlanChatModel(model="gpt-5.4", reasoning_effort="medium")


def test_plan_provider_uses_public_responses_with_scoped_token():
    model = _model()
    captured = {}

    def stream(headers, payload):
        captured.update(headers=headers, payload=payload)
        return {"output": []}

    with patch("deerflow.models.openai_codex_provider.get_siwc_access_token", return_value="siwc-token"), patch.object(ChatGPTPlanChatModel, "_stream_response", side_effect=stream):
        model._call_codex_api(
            [SystemMessage("You are helpful"), HumanMessage("Hello")],
            tools=[{"type": "function", "name": "lookup", "description": "Look up", "parameters": {"type": "object", "properties": {}}}],
        )

    assert model._responses_url() == "https://api.openai.com/v1/responses"
    assert captured["headers"]["Authorization"] == "Bearer siwc-token"
    assert "ChatGPT-Account-ID" not in captured["headers"]
    assert "originator" not in captured["headers"]
    payload = captured["payload"]
    assert payload["instructions"] == "You are helpful"
    assert payload["input"] == [{"role": "user", "content": "Hello"}]
    assert payload["store"] is False and payload["stream"] is True
    assert payload["include"] == ["reasoning.encrypted_content"]
    assert payload["tools"][0]["type"] == "namespace"
    assert payload["tools"][0]["tools"][0]["name"] == "lookup"


def test_plan_provider_preserves_encrypted_reasoning_for_next_turn():
    model = _model()
    reasoning = {"type": "reasoning", "id": "rs_1", "summary": [], "encrypted_content": "ciphertext"}
    response = {"output": [reasoning, {"type": "function_call", "name": "lookup", "arguments": "{}", "call_id": "call_1"}]}
    prior = model._parse_response(response).generations[0].message
    _, items = model._convert_messages([prior, ToolMessage(content="found", tool_call_id="call_1")])
    assert items[0] == reasoning
    assert items[1]["namespace"] == "deerflow"
    assert items[2]["type"] == "function_call_output"


def test_plan_provider_replays_tool_calls_in_namespace():
    model = _model()
    messages = [
        AIMessage(content="", tool_calls=[{"name": "lookup", "args": {"id": 1}, "id": "call_1"}]),
        ToolMessage(content="found", tool_call_id="call_1"),
    ]
    _, items = model._convert_messages(messages)
    assert items[0]["namespace"] == "deerflow"
    assert items[1]["type"] == "function_call_output"


def test_plan_provider_surfaces_streamed_usage_limit():
    import httpx
    import pytest

    model = _model()
    stream = b'data: {"type":"error","error":{"code":"subscription_sharing_usage_limit_exceeded","message":"limit reached"}}\n\n'
    real_client = httpx.Client

    def client_with_error(**kwargs):
        return real_client(transport=httpx.MockTransport(lambda _request: httpx.Response(200, headers={"content-type": "text/event-stream"}, content=stream)), **kwargs)

    with patch("deerflow.models.openai_codex_provider.httpx.Client", side_effect=client_with_error):
        with pytest.raises(RuntimeError, match="ChatGPT plan usage limit reached"):
            model._stream_response({"Authorization": "Bearer dummy"}, {"model": "gpt-6-astra", "store": False, "stream": True})
