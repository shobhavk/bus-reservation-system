from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.api import database, database_manager, schemas
from app.api.models import Booking
import requests
import json

routes = APIRouter(
    prefix="/bookings",
    tags=['Bookings']
)

get_db = database.get_db

@routes.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Booking, db: Session= Depends(get_db)):
    get_response = requests.get(f"http://localhost:8000/inventory/search/{request.bus_route_id}/")
    inventory = json.loads(get_response.content.decode('utf-8'))
    if inventory['available_seats'] > request.number_of_seats:
        return database_manager.create(request, db)
    else:  
        return "cannot create"
    # return database_manager.create(request, db)
