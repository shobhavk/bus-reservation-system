from sqlalchemy.orm import Session
from app.api import model, schema
from fastapi import HTTPException, status

def create(request: schema.BusRoute, db: Session):
    new_route = model.BusRoute(**request.dict())
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return new_route