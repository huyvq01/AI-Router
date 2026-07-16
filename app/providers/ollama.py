from __future__ import annotations

from typing import Any

import httpx

from app.config import settings
from app.providers.base import BaseLLMProvider
from app.providers.models import (
    OllamaGenerateRequest,
    OllamaGenerateResponse,
)
from app.schemas.chat import ChatRequest, ChatResponse


class OllamaProvider(BaseLLMProvider):
    """
    Ollama Provider.

    Responsible for communicating with the Ollama REST API.
    """

    def __init__(self) -> None:
        self._client: httpx.AsyncClient | None = None

    async def startup(self) -> None:
        """Initialize HTTP client."""
        self._client = httpx.AsyncClient(
            base_url=settings.OLLAMA_HOST,
            timeout=settings.OLLAMA_TIMEOUT,
        )

    async def shutdown(self) -> None:
        """Close HTTP client."""
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    def _client_or_raise(self) -> httpx.AsyncClient:
        if self._client is None:
            raise RuntimeError("OllamaProvider has not been started.")

        return self._client

    async def health(self) -> bool:
        """
        Check whether Ollama is available.
        """
        client = self._client_or_raise()

        try:
            response = await client.get("/api/tags")
            response.raise_for_status()
            return True

        except httpx.HTTPError:
            return False

    async def list_models(self) -> list[str]:
        """
        Return available model names.
        """
        client = self._client_or_raise()

        response = await client.get("/api/tags")
        response.raise_for_status()

        payload: dict[str, Any] = response.json()

        return [model["name"] for model in payload.get("models", [])]

    async def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Generate a response using Ollama.
        """
        client = self._client_or_raise()

        request_payload = OllamaGenerateRequest(
            model=request.model,
            prompt=request.prompt,
            stream=request.stream,
            options={
                "temperature": request.temperature,
            },
        )

        response = await client.post(
            "/api/generate",
            json=request_payload.model_dump(),
        )

        response.raise_for_status()

        response_payload = OllamaGenerateResponse.model_validate(response.json())

        return ChatResponse(
            model=response_payload.model,
            content=response_payload.response,
            done=response_payload.done,
            total_duration=response_payload.total_duration,
        )
