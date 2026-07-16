from __future__ import annotations

from pydantic import BaseModel


class RuntimeModelState(BaseModel):
    """
    Runtime state of a model.
    """

    name: str

    loaded: bool = True

    busy: bool = False

    queue_size: int = 0

    latency_ms: float = 0.0

    memory_usage_mb: int = 0


class RuntimeManager:
    """
    Runtime information of all models.
    """

    def __init__(self) -> None:
        self._states: dict[str, RuntimeModelState] = {}

    def get(
        self,
        model_name: str,
    ) -> RuntimeModelState:
        if model_name not in self._states:
            self._states[model_name] = RuntimeModelState(
                name=model_name,
            )

        return self._states[model_name]

    def update(
        self,
        state: RuntimeModelState,
    ) -> None:
        self._states[state.name] = state
