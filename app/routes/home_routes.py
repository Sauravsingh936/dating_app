from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.utils.auth import get_current_user

from app.services.home_service import (
    fetch_home_experts,
    fetch_category_experts,
    fetch_expert_details
)

router = APIRouter(
    prefix="/api/v1/home",
    tags=["Home"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/experts")
def get_home_experts(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return fetch_home_experts(db)


@router.get("/experts/category/{category}")
def get_category_experts(
    category: str,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return fetch_category_experts(
        db,
        category
    )

@router.get("/experts/{expert_id}")
def get_expert_details(
    expert_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return fetch_expert_details(
        db,
        expert_id
    )