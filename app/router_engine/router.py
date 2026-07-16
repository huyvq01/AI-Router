from __future__ import annotations

from app.domain.decision import RouteDecision
from app.router_engine.detector import CapabilityDetector
from app.router_engine.selector import ModelSelector


class Router:
    def __init__(
        self,
        selector: ModelSelector,
        detector: CapabilityDetector,
    ) -> None:
        self._selector = selector
        self._detector = detector

    def route(
        self,
        prompt: str,
    ) -> RouteDecision:
        capability = self._detector.detect(
            prompt,
        )

        selection = self._selector.select(
            capability,
        )

        return RouteDecision(
            provider="ollama",
            model=selection.model.name,
            capability=capability.value,
            score=selection.score,
            reason=selection.reason,
        )
