from __future__ import annotations

from app.router_engine.enums import Capability
from app.router_engine.model import ModelInfo


class ModelRegistry:

    def __init__(self) -> None:
        self._models: dict[str, ModelInfo] = {}

    def load(self) -> None:

        self._models.clear()

        self.register(
            ModelInfo(
                name="qwen2.5-coder:7b",
                capabilities=[
                    Capability.CODE_REVIEW,
                    Capability.CODE_REFACTOR,
                    Capability.CODE_OPTIMIZE,
                    Capability.CODE_GENERATION,
                ],
                context_window=32768,
                speed=5,
                quality=4,
                memory=5,
            )
        )

        self.register(
            ModelInfo(
                name="llama3.2:3b",
                capabilities=[
                    Capability.GENERAL,
                    Capability.DOCUMENTATION,
                ],
                context_window=8192,
                speed=5,
                quality=3,
                memory=2,
            )
        )

    def register(
        self,
        model: ModelInfo,
    ) -> None:
        self._models[model.name] = model

    def all(self) -> list[ModelInfo]:
        return list(self._models.values())