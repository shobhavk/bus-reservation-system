from sqlalchemy.orm import Session
from app.api import models, schemas
from fastapi import HTTPException, status

def create(request: schemas.Booking, db: Session, price: int):
    new_booking = models.Booking(
        source=request.source,
        destination=request.destination,
        price=price,
        bus_route_id=request.bus_route_id,
        number_of_seats=request.number_of_seats,
        booking_date=request.booking_date,
        user_id=request.user_id,
        status='pending',
        total_amount=price * request.number_of_seats
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking