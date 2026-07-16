from __future__ import annotations

from app.providers import (
    ChatRequest,
    ChatResponse,
    provider_manager,
)
from app.router_engine import router_engine


class ChatService:
    """
    High-level chat orchestration.
    """

    async def chat(
        self,
        prompt: str,
    ) -> ChatResponse:
        decision = router_engine.route(
            prompt,
        )

        provider = provider_manager.get(
            decision.provider,
        )

        return await provider.chat(
            ChatRequest(
                model=decision.model,
                prompt=prompt,
            )
        )


chat_service = ChatService()
