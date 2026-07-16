from fastapi import APIRouter

from app.schemas.response import ApiResponse

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("", response_model=ApiResponse)
async def health() -> ApiResponse:
    return ApiResponse(
        data={
            "status": "ok",
        }
    )
