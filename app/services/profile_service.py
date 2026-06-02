from app.repository.profile_repository import (
    get_user_by_id,
    save_user
)

def update_name(
    db,
    user_id,
    data
):
    user = get_user_by_id(
        db,
        user_id
    )

    user.name = data.name

    save_user(db, user)

    return {
        "status": True,
        "message": "Name Updated"
    }

def update_age(
    db,
    user_id,
    data
):
    user = get_user_by_id(
        db,
        user_id
    )

    user.age_group = data.age_group

    save_user(db, user)

    return {
        "status": True,
        "message": "Age Updated"
    }

def update_gender(
    db,
    user_id,
    data
):
    user = get_user_by_id(
        db,
        user_id
    )

    user.gender_preference = data.gender_preference

    save_user(db, user)

    return {
        "status": True,
        "message": "Gender Preference Updated"
    }

def update_mitra_name(
    db,
    user_id,
    data
):
    user = get_user_by_id(
        db,
        user_id
    )

    user.mitra_name = data.mitra_name

    save_user(db, user)

    return {
        "status": True,
        "message": "Mitra Name Updated"
    }

def update_preferences(
    db,
    user_id,
    data
):
    user = get_user_by_id(
        db,
        user_id
    )

    user.preferences = ",".join(
        data.preferences
    )

    save_user(db, user)

    return {
        "status": True,
        "message": "Preferences Updated"
    }