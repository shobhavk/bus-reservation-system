import asyncio
from aio_pika import connect, IncomingMessage, Message
import json
from sqlalchemy.orm import Session
from app.api import database

async def on_message(message: IncomingMessage):
    txt = message.body.decode("utf-8")
    data = json.loads(txt)
    request = {
        'user_id': data['user_id'],
        'booking_id': data['booking_id']
    }
    print("thisis data",data)
    if data['payment_status']  == 'success':
        await database.raw_sql(request)
    else:
        await database.rollback_booking(request)

async def main(loop):
    connection = await connect(host='localhost', loop = loop)

    channel = await connection.channel()

    queue1 = await channel.declare_queue("inventory_updated")
    queue2 = await channel.declare_queue("payment_failed")

    await queue1.consume(on_message, no_ack = True)
    await queue1.consume(on_message, no_ack = True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()