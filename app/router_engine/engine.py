from __future__ import annotations

from app.router_engine.detector import CapabilityDetector
from app.router_engine.registry import ModelRegistry
from app.router_engine.router import Router
from app.router_engine.runtime import RuntimeManager
from app.router_engine.scorer import ModelScorer
from app.router_engine.selector import ModelSelector


class RouterEngine:
    def __init__(self) -> None:
        registry = ModelRegistry()
        registry.load()

        runtime = RuntimeManager()

        scorer = ModelScorer()

        selector = ModelSelector(
            registry,
            runtime,
            scorer,
        )

        detector = CapabilityDetector()

        self._router = Router(
            selector,
            detector,
        )

    def route(
        self,
        prompt: str,
    ):
        return self._router.route(
            prompt,
        )


router_engine = RouterEngine()
