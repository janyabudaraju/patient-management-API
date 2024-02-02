import models
import schemas
from typing import List
from fastapi import FastAPI, HTTPException
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






