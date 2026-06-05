from pydantic import BaseModel


class CreateConversationSchema(
    BaseModel
):
    topic: str


class SendMessageSchema(
    BaseModel
):
    conversation_id: int
    message: str