import asyncio
from aio_pika import connect, IncomingMessage
import json
from sqlalchemy.orm import Session
from app.api import database
import os

async def on_message(message: IncomingMessage):
    txt = message.body.decode("utf-8")
    booking = json.loads(txt)
    request = {
        'booking_id': booking['id'],
        'date_of_payment': booking['booking_date'],
        'number_of_seats': booking['number_of_seats'],
        'bus_route_id': booking['bus_route_id'],
        'user_id': booking['user_id']
    }
    
    await database.raw_sql(request)

async def main(loop):
    connection = await connect(host='rabbitmq', loop = loop)

    channel = await connection.channel()

    queue1 = await channel.declare_queue("booking_created")
    await queue1.consume(on_message, no_ack = True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()