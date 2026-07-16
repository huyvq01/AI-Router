from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    prompt: str

    temperature: float = 0.2

    stream: bool = False

    model: str | None = Field(
        default=None,
        description="Auto selected by Router",
    )


class ChatResponse(BaseModel):
    model: str

    content: str

    done: bool = False

    total_duration: float = 0.0
