from fastapi import FastAPI

from app.api.v1.chat import router as chat_router
from app.api.v1.health import router as health_router
from app.config import settings
from app.core.lifespan import lifespan
from app.exceptions import register_exception_handlers
from app.middleware import RequestLoggingMiddleware


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    app = FastAPI(
        title=settings.APP_NAME,
        version="0.1.0",
        description="Production AI Code Analysis Platform",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    # ===========================
    # Middleware
    # ===========================
    app.add_middleware(RequestLoggingMiddleware)

    # ===========================
    # Exception Handlers
    # ===========================
    register_exception_handlers(app)

    # ===========================
    # Routers
    # ===========================
    app.include_router(health_router)
    app.include_router(chat_router)

    return app
