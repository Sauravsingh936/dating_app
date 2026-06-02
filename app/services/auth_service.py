from app.models.user_model import UserModel

from app.repository.auth_repository import *

from app.utils.password import *

from app.utils.jwt_handler import *


def signup_user(
    db,
    data
):

    existing_user = get_user_by_email(
        db,
        data.email
    )

    if existing_user:
        return {
            "status": False,
            "message": "Email already exists"
        }

    new_user = UserModel(
        name=data.name,
        phone=data.phone,
        email=data.email,
        password=hash_password(
            data.password
        )
    )

    create_user(
        db,
        new_user
    )

    return {
        "status": True,
        "message": "User Registered Successfully"
    }


def login_user(
    db,
    data
):

    user = get_user_by_email(
        db,
        data.email
    )

    if not user:
        return {
            "status": False,
            "message": "Invalid Email"
        }

    if not verify_password(
        data.password,
        user.password
    ):
        return {
            "status": False,
            "message": "Invalid Password"
        }

    token = create_access_token(
        {
            "user_id": user.id,
            "email": user.email
        }
    )

    return {
        "status": True,
        "access_token": token,
        "token_type": "bearer"
    }