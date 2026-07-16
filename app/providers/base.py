from __future__ import annotations

from abc import ABC, abstractmethod

from app.providers.models import (
    ChatRequest,
    ChatResponse,
)


class BaseProvider(ABC):
    @abstractmethod
    async def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Execute chat completion.
        """
