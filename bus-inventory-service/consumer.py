import asyncio
from aio_pika import connect, IncomingMessage, Message
import json
from sqlalchemy.orm import Session
from app.api import database, database_manager, schema
import os

async def on_message(message: IncomingMessage):
    txt = message.body.decode("utf-8")
    data = json.loads(txt)
    request = {
        'bus_route_id': data['bus_route_id'],
        'number_of_seats': data['number_of_seats'],
        'last_updated': data['date_of_payment'],
        'user_id': data['user_id'],
        'booking_id': data['booking_id'],
        'payment_status': data['payment_status']
    }
    await database.raw_sql(request)

async def main(loop):
    rabbit_host = os.getenv("AMQP_HOST")
    connection = await connect(rabbit_host, loop = loop)

    channel = await connection.channel()

    queue1 = await channel.declare_queue("payment_created")
    await queue1.consume(on_message, no_ack = True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()