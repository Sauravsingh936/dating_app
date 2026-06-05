from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func

from app.core.database import Base


class SupportConversationModel(Base):

    __tablename__ = "support_conversations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    topic = Column(
        String(255),
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )