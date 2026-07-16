import pytest
from app.services import chat_service


@pytest.mark.asyncio
async def test_chat():
    response = await chat_service.chat(
        "Say hello",
    )

    assert response.model

    assert response.content
