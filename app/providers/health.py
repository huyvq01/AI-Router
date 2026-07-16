from __future__ import annotations

import httpx

from app.config import settings


class ProviderHealth:
    async def check_ollama(self) -> bool:
        try:
            async with httpx.AsyncClient(
                timeout=5,
            ) as client:
                response = await client.get(
                    f"{settings.ollama_base_url}/api/tags"
                )

                return response.status_code == 200

        except Exception:
            return False


provider_health = ProviderHealth()
