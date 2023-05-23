from contextlib import contextmanager
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from databases import Database
from app.api.config import settings
import warnings
from sqlalchemy.sql import text
from app.api.sender import send_rabbitmq

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        warnings.warn("We somehow failed in a DB operation and auto-rollbacking...")
    finally:
        db.close()

async def raw_sql(request):
    with engine.connect() as con:
        try:    
            data = ({'booking_id': request['booking_id'], 'date_of_payment': request['date_of_payment']})
            statement = text("""INSERT INTO payments(booking_id, date_of_payment) VALUES (:booking_id, :date_of_payment)""")
            con.execute(statement, data)
            await send_rabbitmq(request, 'payment_created')
        except:
            warnings.warn("We somehow failed in a DB operation and auto-rollbacking...")
            await send_rabbitmq(request, 'payment_failed')
