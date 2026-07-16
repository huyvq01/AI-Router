import pytest
from app.providers import ollama_provider
from app.providers.models import ChatRequest


@pytest.mark.asyncio
async def test_chat():
    response = await ollama_provider.chat(
        ChatRequest(
            model="qwen2.5-coder:7b",
            prompt="Hello",
        )
    )

    assert response.model == "qwen2.5-coder:7b"

    assert response.content
