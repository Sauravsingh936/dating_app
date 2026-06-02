from app.models.user_model import UserModel


def get_user_by_email(
    db,
    email
):
    return (
        db.query(UserModel)
        .filter(UserModel.email == email)
        .first()
    )


def create_user(
    db,
    user
):
    db.add(user)
    db.commit()
    db.refresh(user)

    return user