from pydantic import BaseModel

from app.router_engine.model import ModelInfo


class SelectionResult(BaseModel):
    model: ModelInfo

    score: int

    reason: str
