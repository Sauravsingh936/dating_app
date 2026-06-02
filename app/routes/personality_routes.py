from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.personality_schema import (
    PersonalityRequest,
    PersonalityResponse
)
from app.services.personality_service import select_personality

router = APIRouter(
    prefix="/api/v1/personality",
    tags=["Personality"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/select",
    response_model=PersonalityResponse
)
def personality_api(
    data: PersonalityRequest,
    db: Session = Depends(get_db)
):
    return select_personality(db, data)