from app.models.expert_model import ExpertModel


def create_expert(db, expert):

    db.add(expert)

    db.commit()

    db.refresh(expert)

    return expert


def get_all_experts(db):

    return db.query(
        ExpertModel
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


def delete_expert(
    db,
    expert
):

    db.delete(expert)

    db.commit()

def update_expert(db):

    db.commit()    