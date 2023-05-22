from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Date
# from database import Base
from app.api.database import Base
from sqlalchemy.orm import relationship

class Payment(Base):
    __tablename__ = "payments"
    __table_args__= {
        'mysql_engine':'InnoDB'
    }
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer)
    date_of_payment = Column(Date)