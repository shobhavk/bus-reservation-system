import asyncio
from aio_pika import connect, IncomingMessage, Message
import json
import os

async def send_rabbitmq(msg ={}):
    connection = await connect(host='rabbitmq')

    channel = await connection.channel()
    await channel.default_exchange.publish(
        Message(json.dumps(msg).encode("utf-8")),
        routing_key = 'inventory_updated'
    )

    await connection.close()