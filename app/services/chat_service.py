from app.repository.chat_repository import (
    save_chat,
    get_chat_history
)


def send_chat(db, data):

    ai_reply = "Hi, how are you?"

    save_chat(
        db,
        data.user_id,
        data.message,
        ai_reply
    )

    return {
        "status": True,
        "reply": ai_reply
    }


def fetch_chat_history(db, user_id):
    return get_chat_history(db, user_id)