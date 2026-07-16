from app.providers.base import BaseLLMProvider
from app.providers.ollama import OllamaProvider


class ProviderManager:
    def __init__(self) -> None:
        self._provider: BaseLLMProvider | None = None

    async def startup(self) -> None:
        self._provider = self._create_provider()
        await self._provider.startup()

    async def shutdown(self) -> None:
        if self._provider is not None:
            await self._provider.shutdown()

    @property
    def provider(self) -> BaseLLMProvider:
        if self._provider is None:
            raise RuntimeError("ProviderManager has not been started.")

        return self._provider

    def _create_provider(self) -> BaseLLMProvider:
        # Sau này mở rộng:
        # if settings.PROVIDER == "openai":
        #     return OpenAIProvider()
        # if settings.PROVIDER == "vllm":
        #     return VLLMProvider()

        return OllamaProvider()


provider_manager = ProviderManager()
