from app.models.expert_model import ExpertModel


def get_all_experts(db):

    return db.query(
        ExpertModel
    ).all()


def get_experts_by_category(
    db,
    category
):

    return db.query(
        ExpertModel
    ).filter(
        ExpertModel.category == category
    ).all()


def get_expert_by_id(
    db,
    expert_id
):

    return db.query(
        ExpertModel
    ).filter(
        ExpertModel.id == expert_id
    ).first()