from app.router_engine.detector import CapabilityDetector
from app.router_engine.registry import ModelRegistry
from app.router_engine.router import Router
from app.router_engine.runtime import RuntimeManager
from app.router_engine.scorer import ModelScorer
from app.router_engine.selector import ModelSelector


def test_router():
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

    router = Router(
        selector,
        detector,
    )

    decision = router.route(
        "Review this Java code",
    )

    assert decision.model == "qwen2.5-coder:7b"
    assert decision.provider == "ollama"
    assert decision.capability == "code_review"
