from datetime import date
from pydantic import BaseModel

class BusRouteBase(BaseModel):
    source: str
    destination: str
    price: int
    total_seats: int

class BusRoute(BusRouteBase):
    class Config():
        orm_mode = True