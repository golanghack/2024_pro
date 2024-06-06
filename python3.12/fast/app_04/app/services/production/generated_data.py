from fastapi import FastAPI
import random
import string
from app.services.utilities.redis_connector import redis_connection
from app.services.utilities.rabbitmq_connector import connection_rabbitmq

app = FastAPI()

@app.get('/data_gen_and_save')
async def generate_data_and_saving():
    """Create data and save data in redis"""
    
    data = ''.join(random.choices(string.ascii_letters, k=200000))
    r = redis_connection()
    r.set('data', data)
    chan = connection_rabbitmq()
    chan.basic_publish(exchange='', routing_key='data_queue', body=data)
    return {'message': 'Data generated and save in redis database; data sent to service customer'}
    