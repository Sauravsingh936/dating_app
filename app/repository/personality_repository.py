from app.models.personality_model import PersonalityModel


def save_personality(db, data):
    personality = PersonalityModel(
        user_id=data.user_id,
        personality_type=data.personality_type
    )

    db.add(personality)
    db.commit()

    return personality