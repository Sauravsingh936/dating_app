from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.schemas.expert_schema import (
    ExpertCreate,
    ExpertUpdate
)

from app.services.expert_service import (
    create_expert_service,
    get_all_experts_service,
    get_expert_details_service,
    update_expert_service,
    delete_expert_service
)

router = APIRouter(
    prefix="/api/v1/experts",
    tags=["Experts"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("")
def create_expert(
    data: ExpertCreate,
    db: Session = Depends(get_db)
):
    return create_expert_service(
        db,
        data
    )


@router.get("")
def get_all_experts(
    db: Session = Depends(get_db)
):
    return get_all_experts_service(db)


@router.get("/{expert_id}")
def get_expert_details(
    expert_id: int,
    db: Session = Depends(get_db)
):
    return get_expert_details_service(
        db,
        expert_id
    )


@router.put("/{expert_id}")
def update_expert(
    expert_id: int,
    data: ExpertUpdate,
    db: Session = Depends(get_db)
):
    return update_expert_service(
        db,
        expert_id,
        data
    )


@router.delete("/{expert_id}")
def delete_expert(
    expert_id: int,
    db: Session = Depends(get_db)
):
    return delete_expert_service(
        db,
        expert_id
    )