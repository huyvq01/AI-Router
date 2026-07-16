import traceback

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core import app_logger


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(
        request: Request,
        exc: Exception,
    ):
        traceback.print_exc()

        app_logger.exception(exc)

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(exc),  # Chỉ để debug
                "error_code": exc.__class__.__name__,
            },
        )
