from app.models.companion_model import CompanionModel


def get_companions(db):
    return db.query(CompanionModel).all()