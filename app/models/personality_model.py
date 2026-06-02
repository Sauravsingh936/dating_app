from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import Base


class PersonalityModel(Base):
    __tablename__ = "personalities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    personality_type = Column(String(100), nullable=False)

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )