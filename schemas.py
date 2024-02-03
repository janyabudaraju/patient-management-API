from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import date

def validate_sex(sex):
    valid_sexes = ['Male', 'Female', 'Other']
    if sex not in valid_sexes:
        raise ValueError(f"Invalid sex: {sex}")
    return sex

def validate_blood_type(blood_type):
    valid_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    if blood_type not in valid_types:
        raise ValueError(f"Invalid blood type: {blood_type}")
    return blood_type

class Patient(BaseModel):
    patient_id: int
    first_name: str = Field(max_length=100)
    middle_name: Optional[str] = Field(None, max_length=100)
    last_name: str = Field(max_length=100)
    date_of_birth: date
    sex: str
    blood_type: str

    class Config:
        from_attributes = True
    
    _validate_sex = validator('sex', allow_reuse=True)(validate_sex)
    _validate_blood_type = validator('blood_type', allow_reuse=True)(validate_blood_type)
    
class PatientCreate(BaseModel):
    first_name: str = Field(max_length=100)
    middle_name: Optional[str] = Field(None, max_length=100)
    last_name: str = Field(max_length=100)
    date_of_birth: date
    sex: str
    blood_type: str

    _validate_sex = validator('sex', allow_reuse=True)(validate_sex)
    _validate_blood_type = validator('blood_type', allow_reuse=True)(validate_blood_type)

class PatientUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=100)
    middle_name: Optional[str] = Field(None, max_length=100)
    last_name: Optional[str] = Field(None, max_length=100)
    date_of_birth: Optional[date] = None
    sex: Optional[str] = None
    blood_type: Optional[str] = None

    _validate_sex = validator('sex', allow_reuse=True)(validate_sex)
    _validate_blood_type = validator('blood_type', allow_reuse=True)(validate_blood_type)
