from app.router_engine import (
    ModelRegistry,
    ModelScorer,
    ModelSelector,
    RuntimeManager,
)
from app.router_engine.enums import Capability


def test_selector():
    registry = ModelRegistry()
    registry.load()

    runtime = RuntimeManager()

    scorer = ModelScorer()

    selector = ModelSelector(
        registry,
        runtime,
        scorer,
    )

    selection = selector.select(
        Capability.CODE_REVIEW,
    )

    assert selection is not None

    assert selection.model is not None

    assert selection.model.name == "qwen2.5-coder:7b"

    assert selection.score > 0

    assert selection.reason == "Highest score"

    runtime_state = runtime.get(
        selection.model.name,
    )

    score = scorer.score(
        Capability.CODE_REVIEW,
        selection.model,
        runtime_state,
    )

    print(
        selection.model.name,
        score,
    )

    assert score == selection.score
