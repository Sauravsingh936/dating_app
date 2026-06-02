from app.models.expert_model import ExpertModel

from app.repository.expert_repository import (
    create_expert,
    get_all_experts,
    get_expert_by_id,
    delete_expert,
    update_expert
)


def create_expert_service(
    db,
    data
):

    expert = ExpertModel(
        name=data.name,
        city=data.city,
        age=data.age,
        category=data.category,
        language=data.language,
        rating=data.rating,
        price_per_min=data.price_per_min,
        profile_image=data.profile_image,
        is_online=data.is_online
    )

    create_expert(
        db,
        expert
    )

    return {
        "status": True,
        "message": "Expert Created Successfully"
    }


def get_all_experts_service(db):

    experts = get_all_experts(db)

    return {
        "status": True,
        "data": experts
    }


def get_expert_details_service(
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


def delete_expert_service(
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

    delete_expert(
        db,
        expert
    )

    return {
        "status": True,
        "message": "Expert Deleted Successfully"
    }

def update_expert_service(
    db,
    expert_id,
    data
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

    expert.name = data.name
    expert.city = data.city
    expert.age = data.age
    expert.category = data.category
    expert.language = data.language
    expert.rating = data.rating
    expert.price_per_min = data.price_per_min
    expert.profile_image = data.profile_image
    expert.is_online = data.is_online

    update_expert(db)

    return {
        "status": True,
        "message": "Expert Updated Successfully"
    }