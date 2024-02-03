import models
import schemas
from typing import List
from fastapi import FastAPI, HTTPException, Depends, status
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Janya's REST API prototype!!"}

@app.post("/patients/", response_model = schemas.Patient, status_code = status.HTTP_201_CREATED)
async def create_patient(patient_data: schemas.PatientCreate, db: Session = Depends(get_session)):
    db_patient = models.Patient(
        first_name = patient_data.first_name,
        middle_name = patient_data.middle_name,
        last_name = patient_data.last_name,
        date_of_birth = patient_data.date_of_birth,
        sex = patient_data.sex,
        blood_type = patient_data.blood_type
    )
    db.add(db_patient)
    try:
        db.commit()
        db.refresh(db_patient)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating patient: {e}")
    return db_patient

@app.get("/patients/{patient_id}", response_model = schemas.Patient)
async def get_patient(patient_id: int, db: Session = Depends(get_session)):
    db_patient = db.query(models.Patient).get(patient_id)
    if not db_patient:
        raise HTTPException(status_code = 404, detail = f"Patient with id {id} not found!")
    return db_patient

