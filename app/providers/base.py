from abc import ABC, abstractmethod

from app.schemas.chat import ChatRequest, ChatResponse


class BaseLLMProvider(ABC):
    @abstractmethod
    async def startup(self) -> None:
        """Initialize provider resources."""

    @abstractmethod
    async def shutdown(self) -> None:
        """Release provider resources."""

    @abstractmethod
    async def health(self) -> bool: ...

    @abstractmethod
    async def list_models(self) -> list[str]: ...

    @abstractmethod
    async def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse: ...
