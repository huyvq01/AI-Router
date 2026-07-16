from app.router_engine.engine import router_engine


def test_route_selection():
    decision = router_engine.route(
        "Optimize this Python code",
    )

    assert decision.model
    assert decision.score >= 0
    assert decision.reason
