from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
# from database import Base
from app.api.database import Base

class BusRoute(Base):
    __tablename__ = "bus_routes"
    id = Column(Integer, primary_key=True, index=True)
    bus_number = Column(Integer, unique=True)
    source = Column(String(20))
    destination = Column(String(20))
    price = Column(Integer)
    total_seats = Column(Integer)