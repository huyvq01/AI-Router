from app.router_engine.enums import Capability
from app.router_engine.model import ModelInfo
from app.router_engine.runtime import RuntimeModelState
from app.router_engine.scorer import ModelScorer


def test_score():
    scorer = ModelScorer()

    metadata = ModelInfo(
        name="qwen2.5-coder:7b",
        capabilities=[Capability.CODE_REVIEW],
        context_window=32768,
        quality=4,
        speed=5,
        memory=5,
    )

    runtime = RuntimeModelState(
        name="qwen2.5-coder:7b",
        loaded=True,
        busy=False,
        queue_size=0,
        latency_ms=80,
    )

    score = scorer.score(
        Capability.CODE_REVIEW,
        metadata,
        runtime,
    )

    assert score > 100
