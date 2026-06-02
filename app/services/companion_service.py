from app.repository.companion_repository import get_companions


def fetch_companions(db):
    companions = get_companions(db)

    return {
        "status": True,
        "data": companions
    }