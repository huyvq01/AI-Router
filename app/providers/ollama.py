from __future__ import annotations

import httpx

from app.config import settings
from app.providers.base import BaseProvider
from app.providers.exceptions import (
    ProviderConnectionError,
    ProviderResponseError,
    ProviderTimeoutError,
)
from app.providers.models import (
    ChatRequest,
    ChatResponse,
)


class OllamaProvider(BaseProvider):
    """
    Ollama HTTP provider.
    """

    async def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:

        payload = {
            "model": request.model,
            "prompt": request.prompt,
            "stream": False,
        }

        try:
            async with httpx.AsyncClient(
                timeout=settings.ollama_timeout,
            ) as client:

                response = await client.post(
                    f"{settings.ollama_base_url}/api/generate",
                    json=payload,
                )

        except httpx.ConnectError as exc:
            raise ProviderConnectionError(
                "Cannot connect to Ollama."
            ) from exc

        except httpx.TimeoutException as exc:
            raise ProviderTimeoutError(
                "Ollama request timeout."
            ) from exc

        if response.status_code != 200:
            raise ProviderResponseError(
                f"Ollama returned {response.status_code}"
            )

        data = response.json()

        return ChatResponse(
            model=request.model,
            content=data.get("response", ""),
            prompt_tokens=data.get("prompt_eval_count", 0),
            completion_tokens=data.get("eval_count", 0),
            total_tokens=(
                data.get("prompt_eval_count", 0)
                + data.get("eval_count", 0)
            ),
        )


ollama_provider = OllamaProvider()