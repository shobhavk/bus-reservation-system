import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from app.api.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# DATABASE_URL="mysql+mysqlconnector://root:MSService$123@localhost:3306/bus_reservation"

# DATABASE_URL = os.environ['DATABASE_URI']
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# db = Database(DATABASE_URL)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()