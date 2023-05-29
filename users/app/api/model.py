from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date
from app.api.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    email = Column(String(20))
    password = Column(String(100))
    role = Column(String(20))