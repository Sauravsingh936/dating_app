from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import TIMESTAMP

from sqlalchemy.sql import func

from app.core.database import Base


class ExpertModel(Base):

    __tablename__ = "experts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    city = Column(
        String(100),
        nullable=False
    )

    age = Column(
        Integer,
        nullable=False
    )

    category = Column(
        String(50),
        nullable=False
    )

    language = Column(
        String(50),
        nullable=False
    )

    rating = Column(
        Float,
        default=0
    )

    price_per_min = Column(
        Integer,
        nullable=False
    )

    profile_image = Column(
        String(255),
        nullable=True
    )

    is_online = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )