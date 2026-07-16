from app.providers import (
    ollama_provider,
    provider_manager,
)


def test_get_provider():
    provider = provider_manager.get(
        "ollama",
    )

    assert provider is ollama_provider
