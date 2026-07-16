from app.router_engine.engine import router_engine
from app.providers.manager import provider_manager

from app.core.logger import app_logger

decision = router_engine.route(
    request.prompt,
)

app_logger.info(
    f"Selected model={decision.model}, capability={decision.capability}, score={decision.score}"
)

request.model = decision.model


class ChatService:
    async def chat(
        self,
        request: ChatRequest,
    ):
        decision = router_engine.route(
            request.prompt,
        )

        request.model = decision.model

        provider = provider_manager.provider

        return await provider.chat(
            request,
        )
