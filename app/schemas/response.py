from typing import Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    success: bool = True
    message: str = "Success"
    data: Any | None = None


class ApiError(BaseModel):
    success: bool = False
    message: str
    error_code: str
