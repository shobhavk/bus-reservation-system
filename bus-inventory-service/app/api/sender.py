import asyncio
from aio_pika import connect, IncomingMessage, Message
import json
import os

async def send_rabbitmq(msg ={}):
    rabbit_host = os.getenv("AMQP_HOST")
    connection = await connect(host=rabbit_host)

    channel = await connection.channel()
    await channel.default_exchange.publish(
        Message(json.dumps(msg).encode("utf-8")),
        routing_key = 'inventory_updated'
    )

    await connection.close()