from pydantic import BaseModel


class RouteDecision(BaseModel):
    provider: str

    model: str

    capability: str

    score: int

    reason: str | None = None
