import asyncio
from aio_pika import connect, IncomingMessage, Message
import json
import os

async def send_rabbitmq(msg ={}, msg_routing_key = str):
    connection = await connect(host='rabbitmq')
    print("it has come here and routingkey", msg_routing_key)
    channel = await connection.channel()
    
    await channel.default_exchange.publish(
        Message(json.dumps(msg).encode("utf-8")),
        routing_key = msg_routing_key
    )

    await connection.close()