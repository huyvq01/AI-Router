from fastapi import APIRouter

from app.api.models import (
    ChatApiRequest,
    ChatApiResponse,
)
from app.services import chat_service

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatApiResponse,
)
async def chat(
    request: ChatApiRequest,
):
    response = await chat_service.chat(
        request.prompt,
    )

    return ChatApiResponse(
        model=response.model,
        content=response.content,
    )
