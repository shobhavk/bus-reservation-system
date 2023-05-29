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

def show(id: int, db: Session):
    booking = db.query(models.Booking).filter(models.Booking.id == id).first()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Booking with the id {id} is not available")
    return booking

def index(db: Session):
    booking = db.query(models.Booking).all()
    return booking

def destroy(id: int, db: Session):
    booking = db.query(models.Booking).filter(models.Booking.id == id)

    if not booking.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Booking  with id {id} not found")

    booking.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schemas.Booking, db: Session):
    booking = db.query(models.Booking).filter(models.Booking.id == id)

    if not booking.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Booking  with id {id} not found")

    booking.update(dict(request))
    db.commit()
    return 'updated'