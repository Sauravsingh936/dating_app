from pydantic import BaseModel


class ExpertResponse(BaseModel):
    id: int
    name: str
    age: int
    city: str
    category: str
    language: str
    rating: float
    price_per_minute: int
    status: str

    class Config:
        from_attributes = True