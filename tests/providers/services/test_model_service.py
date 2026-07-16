import pytest

from app.providers.services.model_service import (
    ollama_model_service,
)


@pytest.mark.asyncio
async def test_list_models():

    models = await ollama_model_service.list_models()

    assert len(models) > 0

    assert "name" in models[0]