from app.repository.session_repository import create_session


def start_session(db, data):
    create_session(db, data)

    return {
        "status": True,
        "message": "Session Started"
    }