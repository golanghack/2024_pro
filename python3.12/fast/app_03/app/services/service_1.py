import six
import sys
if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves
from fastapi import FastAPI
import redis
import os
import random
import string
from kafka import KafkaProducer, KafkaConsumer


app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", "6379"))
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

producer = KafkaProducer(bootstrap_servers= ['127.0.0.1:9092'])
consumer = KafkaConsumer('topic_name', bootstrap_servers=['127.0.0.1:9092'])

@app.get("/")
async def generate_and_save_data():
    data = ''.join(random.choices(string.ascii_letters, k=200000))
    redis_client.set("data", data)
    producer.send('topic_name', key=b'data_ready', value=b'data')
    return {"message": "Data generated and saved to Redis"}

@app.get("/check_signature")
async def check_signature():
    for message in consumer:
        if message.key == b'signature_valid':
            return {"message": "Signature is valid"}
        else:
            return {"message": "Signature is invalid"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
