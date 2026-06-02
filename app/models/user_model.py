from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.core.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    phone = Column(String(20), unique=True, nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    age_group = Column(String(50), nullable=True)

    gender_preference = Column(String(20), nullable=True)

    mitra_name = Column(String(100), nullable=True)

    preferences = Column(Text, nullable=True)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )