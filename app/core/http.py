from __future__ import annotations

import httpx

from app.config import settings


class HttpClient:
    def __init__(self):
        self.client: httpx.AsyncClient | None = None

    async def startup(self):
        self.client = httpx.AsyncClient(
            timeout=settings.OLLAMA_TIMEOUT,
        )

    async def shutdown(self):
        if self.client:
            await self.client.aclose()


http_client = HttpClient()
