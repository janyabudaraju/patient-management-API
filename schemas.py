from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import date

class Patient(BaseModel):
    patient_id: int
    first_name: str = Field(max_length=100)
    middle_name: Optional[str] = Field(None, max_length=100)
    last_name: str = Field(max_length=100)
    date_of_birth: date
    sex: str = Field(max_length=5)
    blood_type: str = Field(max_length=3)

    class Config:
        orm_mode = True
    
    @validator('sex')
    def validate_sex(cls, sex):
        valid_sexes = ['Male', 'Female', 'Other']
        if sex not in valid_sexes:
            raise ValueError(f"Invalid sex: {sex}")
        return sex
    
    @validator('blood_type')
    def validate_blood_type(cls, blood_type):
        valid_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        if blood_type not in valid_types:
            raise ValueError(f"Invalid blood type: {blood_type}")
        return blood_type
    
class PatientCreate(BaseModel):
    first_name: str = Field(max_length=100)
    middle_name: Optional[str] = Field(None, max_length=100)
    last_name: str = Field(max_length=100)
    date_of_birth: date
    sex: str = Field(max_length=5)
    blood_type: str = Field(max_length=3)

    @validator('sex')
    def validate_sex(cls, sex):
        valid_sexes = ['Male', 'Female', 'Other']
        if sex not in valid_sexes:
            raise ValueError(f"Invalid sex: {sex}")
        return sex
    
    @validator('blood_type')
    def validate_blood_type(cls, blood_type):
        valid_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        if blood_type not in valid_types:
            raise ValueError(f"Invalid blood type: {blood_type}")
        return blood_type