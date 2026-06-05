from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    TIMESTAMP
)

from sqlalchemy.sql import func

from app.core.database import Base


class SupportAttachmentModel(Base):

    __tablename__ = "support_attachments"

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

    image_path = Column(
        String(500)
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )