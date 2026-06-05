from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from fastapi import File

from app.utils.auth import get_current_user

from app.schemas.support_schema import (
    CreateConversationSchema,
    SendMessageSchema
)

from app.services.support_service import (
    fetch_support_topics,
    create_support_conversation,
    fetch_conversation_messages,
    send_support_message,
    fetch_user_conversations,
    upload_support_image
)

from app.core.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/api/v1/support",
    tags=["Support"]
)


@router.get("/topics")
def get_topics():

    return fetch_support_topics()

@router.post("/conversations")
def create_conversation_route(
    data: CreateConversationSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return create_support_conversation(
        db,
        current_user["user_id"],
        data
    )

@router.get("/conversations/{conversation_id}/messages")
def get_messages(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return fetch_conversation_messages(
    db,
    conversation_id,
    current_user["user_id"]
)

@router.post("/messages")
def send_message(
    data: SendMessageSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return send_support_message(
        db,
        data
    )

@router.get("/conversations")
def get_user_conversation_list(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return fetch_user_conversations(
        db,
        current_user["user_id"]
    )

@router.post("/upload-image")
def upload_image(
    conversation_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    return upload_support_image(
        db,
        conversation_id,
        file
    )