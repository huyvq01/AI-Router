from __future__ import annotations

from pydantic import BaseModel


class ChatRequest(BaseModel):
    model: str

    prompt: str

    temperature: float = 0.2


class ChatResponse(BaseModel):
    model: str

    content: str

    prompt_tokens: int = 0

    completion_tokens: int = 0

    total_tokens: int = 0
