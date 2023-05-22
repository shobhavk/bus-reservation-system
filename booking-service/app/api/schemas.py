from datetime import date
from datetime import datetime
from pydantic import BaseModel

class Booking(BaseModel):
    user_id: int
    bus_route_id: int
    source: str
    destination: str
    booking_date: date = datetime.now().date()
    number_of_seats: int
    
    class Config:  # to convert non dict obj to json
        orm_mode = True
