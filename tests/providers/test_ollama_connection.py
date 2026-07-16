import pytest
from app.providers import ollama_provider
from app.providers.models import ChatRequest


@pytest.mark.asyncio
async def test_ollama_connection():
    response = await ollama_provider.chat(
        ChatRequest(
            model="qwen2.5-coder:7b",
            prompt="Say hello",
        )
    )

    assert response.content
