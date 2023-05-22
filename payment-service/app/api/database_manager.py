from sqlalchemy.orm import Session
from app.api import model, schema
from fastapi import HTTPException, status

def create(request: schema.Payment, db: Session):
    new_payment = model.Payment(**request.dict())
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

def show(id: int, db: Session):
    payment = db.query(model.Payment).filter(model.Payment.id == id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Payment with the id {id} is not available")
    return payment

def index(db: Session):
    payments = db.query(model.Payment).all()
    return payments

def destroy(id: int, db: Session):
    payment = db.query(model.Payment).filter(model.Payment.id == id)

    if not payment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Payment with id {id} not found")

    payment.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schema.Payment, db: Session):
    payment = db.query(model.Payment).filter(model.Payment.id == id)

    if not payment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Payment with id {id} not found")

    payment.update(dict(request))
    db.commit()
    return 'updated'