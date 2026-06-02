from app.models.user_model import UserModel


def get_user_by_id(db, user_id):

    return (
        db.query(UserModel)
        .filter(UserModel.id == user_id)
        .first()
    )


def save_user(db, user):

    db.commit()
    db.refresh(user)

    return user