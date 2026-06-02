from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):
    user_id: int
    message: str


class ChatResponse(BaseModel):
    status: bool
    reply: str


class ChatHistory(BaseModel):
    id: int
    user_id: int
    message: str
    reply: str

    class Config:
        from_attributes = True