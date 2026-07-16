from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core import app_logger
from app.providers.manager import provider_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    app_logger.info("Application starting...")

    await provider_manager.startup()

    app_logger.info("Provider initialized.")

    yield

    await provider_manager.shutdown()

    app_logger.info("Application shutting down...")
