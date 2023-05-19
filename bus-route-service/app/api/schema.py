from datetime import date
from pydantic import BaseModel

class BusRoute(BaseModel):
    bus_number: int
    source: str
    destination: str
    price: int
    total_seats: int

    class Config:
        orm_mode = True