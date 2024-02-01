from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4 #why uuid 4?
from enum import Enum

class Sex(str, Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'

class Patient(BaseModel):
    id: UUID # understand optional type
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    middle_name: Optional[str] = Field(min_length=1) # TODO: fix
    sex: Sex