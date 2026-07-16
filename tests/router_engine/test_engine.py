from app.router_engine import router_engine


def test_engine():
    decision = router_engine.route(
        "Review Java source code",
    )

    assert decision.model.startswith("qwen")

    assert decision.provider == "ollama"

    assert decision.capability == "code_review"
