from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.api import database, database_manager, schemas
from app.api.models import Booking
import requests
import json
from aio_pika import connect, Message
from typing import Dict
import asyncio
from fastapi.encoders import jsonable_encoder

routes = APIRouter(
    prefix="/bookings",
    tags=['Bookings']
)

get_db = database.get_db

@routes.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Booking, db: Session= Depends(get_db)):
    bus_route_response = requests.get(f"http://bus-routes:8000/bus_routes/{request.bus_route_id}")
    bus_route = json.loads(bus_route_response.content.decode('utf-8'))
    print("wow busroutes", bus_route)
    # price = 100
    # booking = database_manager.create(request, db, price)
    # booking_json_compatible = jsonable_encoder(booking)
    # await send_rabbitmq(booking_json_compatible)
    inventory_response = requests.get(f"http://bus-inventory:8001/inventory/search/{request.bus_route_id}/")
    inventory = json.loads(inventory_response.content.decode('utf-8'))
    print("wow inventory", inventory)
    if inventory['available_seats'] > request.number_of_seats:
        booking = database_manager.create(request, db, bus_route['price'])
        booking_json_compatible = jsonable_encoder(booking)
        await send_rabbitmq(booking_json_compatible)
        return booking
    else:  
        return "cannot create"
    
async def send_rabbitmq(msg ={}):
    connection = await connect(host='rabbitmq')

    channel = await connection.channel()

    await channel.default_exchange.publish(
        Message(json.dumps(msg).encode("utf-8")),
        routing_key = "booking_created"
    )

    await connection.close()

