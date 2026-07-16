from __future__ import annotations

from app.router_engine.enums import Capability
from app.router_engine.model import ModelInfo
from app.router_engine.runtime import RuntimeModelState


class ModelScorer:
    """
    Calculate score for a candidate model.
    """

    CAPABILITY_WEIGHT = 100
    QUALITY_WEIGHT = 20
    SPEED_WEIGHT = 15
    CONTEXT_WEIGHT = 1
    MEMORY_WEIGHT = 5

    def score(
        self,
        capability: Capability,
        metadata: ModelInfo,
        runtime: RuntimeModelState,
    ) -> int:
        score = 0

        if capability in metadata.capabilities:
            score += self.CAPABILITY_WEIGHT

        score += metadata.quality * self.QUALITY_WEIGHT

        score += metadata.speed * self.SPEED_WEIGHT

        score += (metadata.context_window // 4096) * self.CONTEXT_WEIGHT

        score += metadata.memory * self.MEMORY_WEIGHT

        if runtime.loaded:
            score += 20

        if runtime.busy:
            score -= 40

        score -= runtime.queue_size * 5

        score -= int(
            runtime.latency_ms / 50,
        )

        return score
