from sqlalchemy import Column, Integer, String
from app.core.database import Base


class CompanionModel(Base):
    __tablename__ = "companions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    voice = Column(String(50))