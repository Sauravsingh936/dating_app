from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.companion_schema import CompanionResponse
from app.services.companion_service import fetch_companions

router = APIRouter(
    prefix="/api/v1",
    tags=["Companions"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/companions",
    response_model=CompanionResponse
)
def get_companions_api(
    db: Session = Depends(get_db)
):
    return fetch_companions(db)