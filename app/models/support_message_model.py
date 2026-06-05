from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP
from sqlalchemy.sql import func

from app.core.database import Base


class SupportMessageModel(Base):

    __tablename__ = "support_messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    conversation_id = Column(
        Integer,
        ForeignKey(
            "support_conversations.id"
        )
    )

    sender = Column(
        String(50)
    )

    message = Column(
        Text
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )