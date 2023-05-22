from datetime import date
from datetime import datetime
from pydantic import BaseModel

class Payment(BaseModel):
    booking_id: int
    date_of_payment: date = datetime.now().date()

    class Config():
        orm_mode = True
