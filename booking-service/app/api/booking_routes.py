from typing import List
from fastapi import APIRouter, HTTPException, Depends, status, Request
from sqlalchemy.orm import Session
from app.api import database, database_manager, schemas
from app.api.models import Booking
import requests
import json
from aio_pika import connect, Message
from typing import Dict
import asyncio
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

routes = APIRouter(
    prefix="/bookings",
    tags=['Bookings']
)

get_db = database.get_db

@routes.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Booking, db: Session= Depends(get_db)):
    bus_route_response = requests.get(f"http://bus-routes:8000/bus_routes/{request.bus_route_id}")
    bus_route = json.loads(bus_route_response.content.decode('utf-8'))
    inventory_response = requests.get(f"http://bus-inventory:8001/inventory/search/{request.bus_route_id}/")
    inventory = json.loads(inventory_response.content.decode('utf-8'))
    try:
        if inventory['available_seats'] > request.number_of_seats:
            booking = database_manager.create(request, db, bus_route['price'])
            booking_json_compatible = jsonable_encoder(booking)
            await send_rabbitmq(booking_json_compatible)
            return booking
    except:  
        return "cannot create"
    
async def send_rabbitmq(msg ={}):
    connection = await connect(host='rabbitmq')

    channel = await connection.channel()

    await channel.default_exchange.publish(
        Message(json.dumps(msg).encode("utf-8")),
        routing_key = "booking_created"
    )

    await connection.close()

@routes.get('/', response_model=List[schemas.Booking])
# def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def all(db: Session = Depends(get_db)):
    return database_manager.index(db)

@routes.get('/{id}', status_code=200, response_model=schemas.Booking)
# def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def show(id: int, db: Session = Depends(get_db)):
    return database_manager.show(id, db)

@routes.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Booking, db: Session = Depends(get_db)):
    return database_manager.update(id, request, db)

# @routes.post('/login', status_code=200)
def get_token(request: OAuth2PasswordRequestForm = Depends()):
    data = {'username': request.username, 'password': request.password}
    response =  requests.post(
        f"http://user-service:8004/user/login", data
    )

    print("wow token", response)
    if response.status_code == 200:
        print("this is token", response.text)
        return response.text, None
    else:
        return None, (response.text, response.status_code)

# def validate_token(token):

@routes.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def destroy(id: int, db: Session = Depends(get_db), current_user = Depends(get_token)):
    return database_manager.destroy(id, db)
