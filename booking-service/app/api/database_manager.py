from sqlalchemy.orm import Session
from app.api import models, schemas
from fastapi import HTTPException, status

def create(request: schemas.Booking, db: Session):
    new_booking = models.Booking(**request.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking