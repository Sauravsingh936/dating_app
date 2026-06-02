from pydantic import BaseModel


class ExpertCreate(BaseModel):

    name: str

    city: str

    age: int

    category: str

    language: str

    rating: float

    price_per_min: int

    profile_image: str | None = None

    is_online: bool = True


class ExpertUpdate(BaseModel):

    name: str

    city: str

    age: int

    category: str

    language: str

    rating: float

    price_per_min: int

    profile_image: str | None = None

    is_online: bool


class ExpertResponse(BaseModel):

    id: int

    name: str

    city: str

    age: int

    category: str

    language: str

    rating: float

    price_per_min: int

    profile_image: str | None

    is_online: bool

    class Config:
        from_attributes = True