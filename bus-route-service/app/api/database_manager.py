from sqlalchemy.orm import Session
from app.api import model, schema
from fastapi import HTTPException, status

def create(request: schema.BusRoute, db: Session):
    new_route = model.BusRoute(**request.dict())
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return new_route

def show(id: int, db: Session):
    bus_route = db.query(model.BusRoute).filter(model.BusRoute.id == id).first()
    if not bus_route:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bus route number with the id {id} is not available")
    return bus_route

def index(db: Session):
    bus_routes = db.query(model.BusRoute).all()
    return bus_routes

def destroy(id: int, db: Session):
    bus_route = db.query(model.BusRoute).filter(model.BusRoute.id == id)

    if not bus_route.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bus route number with id {id} not found")

    bus_route.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schema.BusRoute, db: Session):
    bus_route = db.query(model.BusRoute).filter(model.BusRoute.id == id)

    if not bus_route.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bus route with id {id} not found")

    bus_route.update(dict(request))
    db.commit()
    return 'updated'