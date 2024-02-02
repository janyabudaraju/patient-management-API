from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite:///./patients.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False}) # TODO: validate parameters

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

