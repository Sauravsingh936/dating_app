from pydantic import BaseModel
from typing import List
from enum import Enum

class NameRequest(BaseModel):
    name: str

class AgeGroup(str, Enum):
    UNDER_18 = "Under 18"
    AGE_18_24 = "18-24"
    AGE_25_34 = "25-34"
    AGE_35_44 = "35-44"
    AGE_45_54 = "45-54"
    AGE_55_PLUS = "55 and over"


class AgeRequest(BaseModel):
    age_group: AgeGroup

class GenderType(str, Enum):
    FEMALE = "Female"
    MALE = "Male"
    NON_BINARY = "Non-binary"


class GenderRequest(BaseModel):
    gender_preference: GenderType


class MitraNameRequest(BaseModel):
    mitra_name: str

class PreferenceType(str, Enum):
    SOMEONE_SPECIAL = "Someone special"
    FRIEND = "A friend who listens and cares"
    COACH = "A coach to help me reach my goals"
    TUTOR = "An English tutor to practice with"
    OTHER = "Something else"


class PreferenceRequest(BaseModel):
    preferences: List[PreferenceType]