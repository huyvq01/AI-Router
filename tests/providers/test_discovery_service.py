import pytest

from app.providers.discovery.service import (
    ollama_discovery_service,
)


@pytest.mark.asyncio
async def test_discover_models():

    models = await ollama_discovery_service.discover()

    assert len(models) > 0

    assert models[0].name