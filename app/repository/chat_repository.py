from app.models.chat_model import ChatModel


def save_chat(db, user_id, message, reply):
    chat = ChatModel(
        user_id=user_id,
        message=message,
        reply=reply
    )

    db.add(chat)
    db.commit()

    return chat


def get_chat_history(db, user_id):
    return (
        db.query(ChatModel)
        .filter(ChatModel.user_id == user_id)
        .all()
    )