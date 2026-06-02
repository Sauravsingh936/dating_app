from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.utils.auth import get_current_user

from app.schemas.profile_schema import (
    NameRequest,
    AgeRequest,
    GenderRequest,
    MitraNameRequest,
    PreferenceRequest
)

from app.services.profile_service import (
    update_name,
    update_age,
    update_gender,
    update_mitra_name,
    update_preferences
)

router = APIRouter(
    prefix="/api/v1/profile",
    tags=["Profile"]
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@router.post("/name")
def save_name(
    data: NameRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_name(
        db,
        current_user["user_id"],
        data
    )

@router.post("/age")
def save_age(
    data: AgeRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_age(
        db,
        current_user["user_id"],
        data
    )

@router.post("/preferences")
def save_preferences(
    data: PreferenceRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_preferences(
        db,
        current_user["user_id"],
        data
    )

@router.post("/gender")
def save_gender(
    data: GenderRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_gender(
        db,
        current_user["user_id"],
        data
    )

@router.post("/mitra_name")
def save_mitra_name(
    data: MitraNameRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_mitra_name(
        db,
        current_user["user_id"],
        data
    )
