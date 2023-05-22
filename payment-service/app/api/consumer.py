import asyncio
from aio_pika import connect, IncomingMessage
import json
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.api import database, database_manager, schema
from app.api.model import Payment

get_db = database.get_db

async def on_message(message: IncomingMessage):
    txt = message.body.decode("utf-8")
    booking = json.loads(txt)
    request = {
        'booking_id': booking['id'],
        'date_of_payment': booking['booking_date']
    }
    database_manager.create(request, Session= Depends(get_db))


async def main(loop):
    connection = await connect(host='localhost', loop = loop)

    channel = await connection.channel()

    queue = await channel.declare_queue("booking_created")

    await queue.consume(on_message, no_ack = True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()