from app.core.logger import app_logger
from app.providers.manager import provider_manager
from app.providers.models import ChatRequest
from app.router_engine.engine import router_engine


class ChatService:
    async def chat(
        self,
        request: ChatRequest,
    ):
        decision = router_engine.route(
            request.prompt,
        )

        app_logger.info(
            f"Selected model={decision.model}, "
            f"capability={decision.capability}, "
            f"score={decision.score}"
        )

        request.model = decision.model

        provider = provider_manager.provider

        return await provider.chat(request)


chat_service = ChatService()
