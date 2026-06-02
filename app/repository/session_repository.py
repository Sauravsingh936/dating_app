from app.models.session_model import SessionModel


def create_session(db, data):
    session = SessionModel(
        device_id=data.device_id
    )

    db.add(session)
    db.commit()

    return session