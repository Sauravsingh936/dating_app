from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import SessionLocal
from app.schemas.chat_schema import (
    ChatRequest,
    ChatResponse,
    ChatHistory
)

from app.services.chat_service import (
    send_chat,
    fetch_chat_history
)

router = APIRouter(
    prefix="/api/v1/chat",
    tags=["Chat"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/send",
    response_model=ChatResponse
)
def send_chat_api(
    data: ChatRequest,
    db: Session = Depends(get_db)
):
    return send_chat(db, data)


@router.get(
    "/history/{user_id}",
    response_model=List[ChatHistory]
)
def get_chat_history_api(
    user_id: int,
    db: Session = Depends(get_db)
):
    return fetch_chat_history(db, user_id)