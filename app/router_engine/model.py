from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from app.router_engine.enums import Capability


class ModelInfo(BaseModel):
    model_config = ConfigDict(
        frozen=True,
    )

    name: str

    capabilities: list[Capability]

    context_window: int

    speed: int

    quality: int

    memory: int
