from pydantic import BaseModel


class SessionRequest(BaseModel):
    device_id: str


class SessionResponse(BaseModel):
    status: bool
    message: str