from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base


class ChatModel(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    message = Column(Text, nullable=False)
    reply = Column(Text, nullable=False)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )