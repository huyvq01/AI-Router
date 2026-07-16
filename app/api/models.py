from pydantic import BaseModel


class ChatApiRequest(BaseModel):
    prompt: str


class ChatApiResponse(BaseModel):
    model: str
    content: str
