import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from app.api.config import settings
import warnings
from app.api import sender

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
            route_id = request['bus_route_id']
            select_query = f'SELECT available_seats FROM bus_inventory WHERE bus_route_id={route_id}'
            current_available_seats = con.execute(select_query)
            total_seats = []
            for row in current_available_seats:
                total_seats.append(row[0])
            update_seats = total_seats[0] - request['number_of_seats']
            sql_update = "UPDATE bus_inventory SET available_seats=%s, last_updated=%s WHERE bus_route_id=%s"
            val = (update_seats, request['last_updated'], route_id)
            # data = ({'booking_id': request['booking_id'], 'last_updated': request['booking_date'], })
            con.execute(sql_update, val)
            await sender.send_rabbitmq(request)
        except:
            warnings.warn("We somehow failed in a DB operation and auto-rollbacking...")
