from typing import List
from fastapi import APIRouter, HTTPException, Depends, status, Request
from sqlalchemy.orm import Session
from app.api import database, database_manager, schema
from app.api.model import BusInventory

routes = APIRouter(
    prefix="/inventory",
    tags=['Inventory']
)


get_db = database.get_db

@routes.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schema.BusInventory, db: Session= Depends(get_db)):
   return database_manager.create(request, db)      

@routes.get('/', response_model=List[schema.BusInventory])
# def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def all(db: Session = Depends(get_db)):
    return database_manager.index(db)

@routes.get('/{id}', status_code=200, response_model=schema.BusInventory)
# def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def show(id: int, db: Session = Depends(get_db)):
    return database_manager.show(id, db)

@routes.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def destroy(id: int, db: Session = Depends(get_db)):
    return database_manager.destroy(id, db)


@routes.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.BusInventory, db: Session = Depends(get_db)):
    return database_manager.update(id, request, db)

@routes.get('/search/{bus_route_id}', status_code=200, response_model=schema.BusInventory)
def get_total_seats(bus_route_id: int, db: Session = Depends(get_db)):
    print("thisis request", bus_route_id)
    return database_manager.get_total_seats(bus_route_id, db)