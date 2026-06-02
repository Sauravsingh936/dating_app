from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.session_schema import (
    SessionRequest,
    SessionResponse
)
from app.services.session_service import start_session

router = APIRouter(
    prefix="/api/v1/session",
    tags=["Session"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/start",
    response_model=SessionResponse
)
def create_session_api(
    data: SessionRequest,
    db: Session = Depends(get_db)
):
    return start_session(db, data)