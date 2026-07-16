from __future__ import annotations

import httpx

from app.providers.config import ollama_config


class OllamaModelService:
    """
    Discover models from Ollama.
    """

    async def list_models(
        self,
    ) -> list[dict]:

        async with httpx.AsyncClient(
            timeout=ollama_config.timeout,
        ) as client:

            response = await client.get(
                f"{ollama_config.base_url}/api/tags",
            )

            response.raise_for_status()

            data = response.json()

            return data.get(
                "models",
                [],
            )


ollama_model_service = OllamaModelService()