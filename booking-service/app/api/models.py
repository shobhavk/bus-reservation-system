# from sqlalchemy.schema import Column
# from sqlalchemy.types import String, Integer, Text
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date
from app.api.database import Base
from sqlalchemy.orm import relationship

class Booking(Base):
    __tablename__ = "bookings"
    __table_args__= {
        'mysql_engine':'InnoDB'
    }
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String(20))
    destination = Column(String(20))
    number_of_seats = Column(Integer)
    bus_route_id = Column(Integer)
    booking_date = Column(Date)
    user_id = Column(Integer)
    status = Column(String(20), default='Pending')
    total_amount = Column(Integer)
    price = Column(Integer)
    passenger = relationship("Passenger", back_populates="bookings")
 
class Passenger(Base):
    __tablename__ = "passengers"
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    user_id = Column(Integer)
    bookings = relationship("Booking", back_populates="passenger")
