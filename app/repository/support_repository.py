from app.models.support_conversation_model import SupportConversationModel 
from app.models.support_message_model import SupportMessageModel
from app.models.support_attachment_model import SupportAttachmentModel
    

SUPPORT_TOPICS = [
    "Recharge Related Issues",
    "Did not receive cashback/discount",
    "User ID Report/Block Issues"
]

def get_support_topics():

    return SUPPORT_TOPICS

def create_conversation(
    db,
    user_id,
    topic
):

    conversation = SupportConversationModel(
        user_id=user_id,
        topic=topic
    )

    db.add(conversation)

    db.commit()

    db.refresh(conversation)

    return conversation

def create_message(
    db,
    conversation_id,
    sender,
    message
):

    msg = SupportMessageModel(
        conversation_id=conversation_id,
        sender=sender,
        message=message
    )

    db.add(msg)

    db.commit()

    db.refresh(msg)

    return msg

def get_conversation_messages(
    db,
    conversation_id
):

    return db.query(
        SupportMessageModel
    ).filter(
        SupportMessageModel.conversation_id == conversation_id
    ).all()

def get_user_conversations(
    db,
    user_id
):

    return db.query(
        SupportConversationModel
    ).filter(
        SupportConversationModel.user_id == user_id
    ).all()

def get_conversation_by_id(
    db,
    conversation_id
):

    return db.query(
        SupportConversationModel
    ).filter(
        SupportConversationModel.id == conversation_id
    ).first()

def create_attachment(
    db,
    conversation_id,
    image_path
):

    attachment = SupportAttachmentModel(
        conversation_id=conversation_id,
        image_path=image_path
    )

    db.add(attachment)

    db.commit()

    db.refresh(attachment)

    return attachment

def get_attachments_by_conversation(
    db,
    conversation_id
):

    return db.query(
        SupportAttachmentModel
    ).filter(
        SupportAttachmentModel.conversation_id == conversation_id
    ).all()