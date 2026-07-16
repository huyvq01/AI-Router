import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.core.logger import app_logger
from app.middleware.request_context import set_request_id


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next,
    ) -> Response:
        request_id = str(uuid.uuid4())

        set_request_id(request_id)

        logger = app_logger.bind(request_id=request_id)

        start = time.perf_counter()

        logger.info(f"Incoming {request.method} {request.url.path}")

        try:
            response = await call_next(request)

        except Exception:
            logger.exception("Unhandled exception")

            raise

        duration = (time.perf_counter() - start) * 1000

        response.headers["X-Request-ID"] = request_id

        logger.info(
            f"Completed {request.method} {request.url.path} "
            f"{response.status_code} "
            f"{duration:.2f} ms"
        )

        return response
