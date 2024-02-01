from fastapi import FastAPI, HTTPException
from model import Patient

app = FastAPI()

patients = []

@app.get("/")
def read_all():
    return patients

@app.post("/")
def add_patient(patient: Patient):
    patients.append(patient)
    return patient

