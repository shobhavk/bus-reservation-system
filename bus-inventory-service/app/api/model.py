from sqlalchemy.schema import Column
from sqlalchemy import Column, Integer, String, Date
# from database import Base
from app.api.database import Base

class BusInventory(Base):
    __tablename__ = "bus_inventory"
    id = Column(Integer, primary_key=True, index=True)
    bus_route_id = Column(Integer)
    available_seats = Column(Integer)
    last_updated = Column(Date)

