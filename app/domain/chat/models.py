from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatSession(BaseModel):
    messages: list[ChatMessage] = []
