from app.router_engine.runtime import (
    RuntimeManager,
    RuntimeModelState,
)


def test_runtime_update():
    runtime = RuntimeManager()

    runtime.update(
        RuntimeModelState(
            name="qwen2.5-coder:7b",
            loaded=True,
            busy=False,
            queue_size=0,
        )
    )

    assert runtime.get("qwen2.5-coder:7b") is not None
