import pytest
from app.services import chat_service


@pytest.mark.asyncio
async def test_chat():
    response = await chat_service.chat(
        "Review this Java code",
    )

    assert response.model

    assert response.content
