from app.repository.personality_repository import save_personality


def select_personality(db, data):
    save_personality(db, data)

    return {
        "status": True,
        "message": "Personality Saved"
    }