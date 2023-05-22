from sqlalchemy.orm import Session
from app.api import model, schema
from fastapi import HTTPException, status

def create(request: schema.BusInventory, db: Session):
    new_inventory = model.BusInventory(**request.dict())
    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory

def show(id: int, db: Session):
    inventory = db.query(model.BusInventory).filter(model.BusInventory.id == id).first()
    if not inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bus inventory number with the id {id} is not available")
    return inventory

def index(db: Session):
    inventory = db.query(model.BusInventory).all()
    return inventory

def destroy(id: int, db: Session):
    inventory = db.query(model.BusInventory).filter(model.BusInventory.id == id)

    if not inventory.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bus inventory number with id {id} not found")

    inventory.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schema.BusInventory, db: Session):
    inventory = db.query(model.BusInventory).filter(model.BusInventory.id == id)

    if not inventory.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bus route with id {id} not found")

    inventory.update(dict(request))
    db.commit()
    return 'updated'

def get_total_seats(bus_route_id: int, db: Session):
    inventory = db.query(model.BusInventory).filter(model.BusInventory.bus_route_id == bus_route_id).first()
    if not inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bus route number with the id {id} is not available")
    return inventory