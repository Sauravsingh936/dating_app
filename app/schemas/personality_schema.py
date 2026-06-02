from pydantic import BaseModel


class PersonalityRequest(BaseModel):
    user_id: int
    personality_type: str


class PersonalityResponse(BaseModel):
    status: bool
    message: str