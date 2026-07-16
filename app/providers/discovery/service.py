from __future__ import annotations

import httpx

from app.config import settings
from app.providers.discovery.models import OllamaModel


class OllamaDiscoveryService:

    async def discover(
        self,
    ) -> list[OllamaModel]:

        async with httpx.AsyncClient(
            timeout=ollama_config.timeout,
        ) as client:

            response = await client.get(
                f"{ollama_config.base_url}/api/tags"
            )

            response.raise_for_status()

            payload = response.json()

        models: list[OllamaModel] = []

        for item in payload.get(
            "models",
            [],
        ):

            details = item.get(
                "details",
                {},
            )

            models.append(

                OllamaModel(
                    name=item["name"],
                    context_window=details.get(
                        "context_length",
                        0,
                    ),
                    family=details.get(
                        "family",
                        "",
                    ),
                    parameter_size=details.get(
                        "parameter_size",
                        "",
                    ),
                    quantization=details.get(
                        "quantization_level",
                        "",
                    ),
                )

            )

        return models


ollama_discovery_service = OllamaDiscoveryService()