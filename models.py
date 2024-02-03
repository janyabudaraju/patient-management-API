from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship, validates
from sqlalchemy.orm import Mapped
from typing import List
from database import Base

class Patient(Base):
    __tablename__ = 'patients'
    patient_id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100))
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    sex = Column(String(50), nullable=False)
    blood_type = Column(String(3), nullable=False)
    # visits: Mapped[List["HospitalVisit"]] = relationship("HospitalVisit", back_populates="patient")

    @validates('sex')
    def validate_sex(self, key, sex):
        valid_sexes = ['Male', 'Female', 'Other']
        if sex not in valid_sexes:
            raise ValueError(f"Invalid sex: {sex}")
        return sex
    
    @validates('blood_type')
    def validate_blood_type(self, key, blood_type):
        valid_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        if blood_type not in valid_types:
            raise ValueError(f"Invalid blood type: {blood_type}")
        return blood_type

# class HospitalVisit(Base):
#     visit_id = Column(Integer, primary_key=True)
#     visit_cause = Column(Text)
#     visit_date = Column(Date, nullable=False)
#     patient: Mapped["Patient"] = relationship(back_populates="visits")
#     patient_id: Column(Integer, ForeignKey('patients.patient_id'))