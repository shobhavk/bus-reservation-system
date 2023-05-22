from datetime import date
from datetime import datetime
from pydantic import BaseModel

class BusInventory(BaseModel):
    last_updated: date = datetime.now().date()
    bus_route_id: int
    available_seats: int

    class Config():
        orm_mode = True