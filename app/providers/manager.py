from __future__ import annotations

from app.core import app_logger
from app.providers.base import BaseProvider
from app.providers.health import provider_health
from app.providers.ollama import ollama_provider


class ProviderManager:
    """
    Manage all available LLM providers.
    """

    def __init__(self) -> None:
        # Providers are always registered.
        self._providers: dict[str, BaseProvider] = {
            "ollama": ollama_provider,
        }

    async def startup(self) -> None:
        """
        Perform startup checks.
        """

        if await provider_health.check_ollama():
            app_logger.info("Ollama provider is ready.")
        else:
            app_logger.warning("Cannot connect to Ollama.")

    async def shutdown(self) -> None:
        """
        Cleanup resources.

        Hiện tại chưa cần làm gì.
        """
        pass

    def get(
        self,
        name: str,
    ) -> BaseProvider:
        try:
            return self._providers[name]
        except KeyError as exc:
            raise ValueError(f"Provider '{name}' is not registered.") from exc

    @property
    def providers(self) -> dict[str, BaseProvider]:
        return self._providers


provider_manager = ProviderManager()
