import asyncio
from aio_pika import connect, IncomingMessage, Message
import json

async def send_rabbitmq(queue_msg ={}, msg_routing_key = str):
    connection = await connect(host='localhost')
    print("it has come here and routingkey", msg_routing_key)
    channel = await connection.channel()
    if msg_routing_key == 'payment_created':
        msg = queue_msg
    else:
        msg = {'Error': 'payment_failed'}
    
    await channel.default_exchange.publish(
        Message(json.dumps(msg).encode("utf-8")),
        routing_key = msg_routing_key
    )

    await connection.close()