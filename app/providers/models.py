from typing import Any

from pydantic import BaseModel, Field


class OllamaGenerateRequest(BaseModel):
    model: str

    prompt: str

    stream: bool = False

    options: dict[str, Any] = Field(default_factory=dict)


class OllamaGenerateResponse(BaseModel):
    model: str

    response: str

    done: bool

    total_duration: float = 0.0
