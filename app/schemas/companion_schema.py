from pydantic import BaseModel
from typing import List


class CompanionData(BaseModel):
    id: int
    name: str
    voice: str

    class Config:
        from_attributes = True


class CompanionResponse(BaseModel):
    status: bool
    data: List[CompanionData]