from __future__ import annotations

import httpx

from app.providers.config import ollama_config


class ProviderHealth:
    async def check_ollama(self) -> bool:
        try:
            async with httpx.AsyncClient(
                timeout=5,
            ) as client:
                response = await client.get(
                    f"{ollama_config.base_url}/api/tags",
                )

                return response.status_code == 200

        except Exception:
            return False


provider_health = ProviderHealth()
