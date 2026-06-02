from app.repository.home_repository import (
    get_all_experts,
    get_experts_by_category,
    get_expert_by_id
)


def fetch_home_experts(db):

    experts = get_all_experts(db)

    return {
        "status": True,
        "data": experts
    }


def fetch_category_experts(
    db,
    category
):

    experts = get_experts_by_category(
        db,
        category
    )

    return {
        "status": True,
        "data": experts
    }


def fetch_expert_details(
    db,
    expert_id
):

    expert = get_expert_by_id(
        db,
        expert_id
    )

    if not expert:
        return {
            "status": False,
            "message": "Expert Not Found"
        }

    return {
        "status": True,
        "data": expert
    }