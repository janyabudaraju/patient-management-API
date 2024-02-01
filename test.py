from fastapi import FastAPI, HTTPException
from model import Patient

app = FastAPI()

patients = [] # think abt making a faster data struct

@app.get("/")
def read_all():
    return patients

@app.post("/")
def add_patient(patient: Patient):
    patients.append(patient)
    return patient

@app.put("/{patient_id}")
def update_patient(patient: Patient):
    for i, p in enumerate(patients):
        if(patient.id == p.id):
            patients[i] = patient
            return patient
    raise HTTPException(status_code=404, detail="Patient does not exist.")
