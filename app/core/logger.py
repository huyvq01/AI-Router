import sys
from pathlib import Path

from loguru import logger

from app.config import settings

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "{extra[request_id]} | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message}</level>"
)

logger.remove()

logger.add(
    sys.stdout,
    level=settings.LOG_LEVEL,
    format=LOG_FORMAT,
    enqueue=True,
    backtrace=False,
    diagnose=False,
    colorize=True,
)

logger.add(
    LOG_DIR / "application.log",
    level=settings.LOG_LEVEL,
    format=LOG_FORMAT,
    rotation="50 MB",
    retention="30 days",
    compression="zip",
    enqueue=True,
    backtrace=False,
    diagnose=False,
)

app_logger = logger.bind(request_id="-")
