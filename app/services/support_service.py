import os
import shutil
from app.repository.support_repository import (
    get_support_topics,
    create_conversation,
    create_message,
    get_conversation_messages,
    get_user_conversations,
    get_conversation_by_id,
    create_attachment,
    get_attachments_by_conversation
)

from app.utils.support_replies import SUPPORT_REPLIES,generate_chat_reply


def fetch_support_topics():

    return {
        "status": True,
        "data": get_support_topics()
    }


def create_support_conversation(
    db,
    user_id,
    data
):

    conversation = create_conversation(
        db,
        user_id,
        data.topic
    )

    reply = SUPPORT_REPLIES.get(
        data.topic,
        "Thank you for contacting support."
    )

    create_message(
        db,
        conversation.id,
        "support",
        reply
    )

    return {
        "status": True,
        "conversation_id": conversation.id,
        "topic": conversation.topic
    }

def fetch_conversation_messages(
    db,
    conversation_id,
    user_id
):

    conversation = get_conversation_by_id(
        db,
        conversation_id
    )

    if not conversation:
        return {
            "status": False,
            "message": "Conversation Not Found"
        }

    if conversation.user_id != user_id:
        return {
            "status": False,
            "message": "Unauthorized"
        }

    messages = get_conversation_messages(
        db,
        conversation_id
    )

    attachments = get_attachments_by_conversation(
        db,
        conversation_id
    )

    return {
        "status": True,
        "messages": messages,
        "attachments": attachments
    }
def send_support_message(
    db,
    data
):

    create_message(
        db,
        data.conversation_id,
        "user",
        data.message
    )

    support_reply = generate_chat_reply(
    data.message
)
    create_message(
        db,
        data.conversation_id,
        "support",
        support_reply
    )

    return {
        "status": True,
        "message": "Message Sent"
    }

def fetch_user_conversations(
    db,
    user_id
):

    conversations = get_user_conversations(
        db,
        user_id
    )

    return {
        "status": True,
        "data": conversations
    }

def upload_support_image(
    db,
    conversation_id,
    file
):

    filename = file.filename

    file_path = (
        f"uploads/{filename}"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    attachment = create_attachment(
        db,
        conversation_id,
        file_path
    )

    return {
        "status": True,
        "image_id": attachment.id,
        "image_path": attachment.image_path
    }