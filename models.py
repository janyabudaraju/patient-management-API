from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, validates
from sqlalchemy.orm import Mapped
from typing import List

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    patient_id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    sex = Column(String(50), nullable=False)
    visits: Mapped[List["HospitalVisit"]] = relationship("HospitalVisit", back_populates="patient")

class HospitalVisit(Base):
    visit_id = Column(Integer, primary_key=True)
    visit_cause = Column(Text)
    visit_date = Column(Date, nullable=False)
    patient: Mapped["Patient"] = relationship(back_populates="visits")
    patient_id: Column(Integer, ForeignKey('patients.id'))

@validates('sex')
def validate_sex(self, key, sex):
    valid_sexes = ['Male', 'Female', 'Other']
    if sex not in valid_sexes:
        raise ValueError("Invalid sex")
    return sex