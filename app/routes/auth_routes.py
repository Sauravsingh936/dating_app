from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.schemas.auth_schema import *

from app.services.auth_service import *

from app.utils.auth import get_current_user

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/signup")
def signup(
    data: SignupRequest,
    db: Session = Depends(get_db)
):
    return signup_user(
        db,
        data
    )


@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    return login_user(
        db,
        data
    )

@router.get("/me")
def get_me(
    current_user=Depends(get_current_user)
):
    return current_user