from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from app.api.config import settings
import warnings
from sqlalchemy.sql import text

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def raw_sql(request):
    with engine.connect() as con:
        try:
            sql_update = "UPDATE bookings SET status=%s WHERE id=%s"
            val = ('confirmed', request['booking_id'])
            con.execute(sql_update, val)
            data = ({'booking_id': request['booking_id'], 'user_id': request['user_id']})
            passenger = text("""INSERT INTO passengers(booking_id, user_id) VALUES (:booking_id, :user_id)""")
            con.execute(passenger, data)
        except:
            warnings.warn("We somehow failed in a DB operation and auto-rollbacking...")

async def rollback_booking(request):
    with engine.connect() as con:
            try:
                sql_delete = "DELETE FROM bookings WHERE id=%s"
                val = (request['booking_id'])
                con.execute(sql_delete, val)
            except:
                warnings.warn("We somehow failed in a DB operation and auto-rollbacking...")    
