from fastapi import FastAPI, HTTPException
from model import Patient
from uuid import UUID

app = FastAPI()

patients = [] # TODO : think abt making a faster data struct

@app.get("/")
def read_all():
    return patients

@app.post("/")
def add_patient(patient: Patient):
    patients.append(patient)
    return patient

@app.put("/{patient_id}")
def update_patient(patient_id: UUID, patient: Patient):
    for i, p in enumerate(patients):
        if(patient.id == p.id):
            patients[i] = patient
            return patient
    raise HTTPException(status_code=404, detail=f"Patient {patient_id} does not exist.")

def delete_patient(patient_id: UUID, patient: Patient):
    for i, p in enumerate(patients):
        if(patient.id == p.id):
            del patients[i]
            return f"ID: {patient.id} deleted"
    raise HTTPException(status_code=404, detail=f"Patient {patient_id} does not exist.")
