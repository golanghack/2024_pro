from kafka import KafkaProducer, KafkaConsumer
import redis
import os
import ecdsa
from ecdsa import SigningKey, NIST256p
import base64

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", "6379"))
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

producer = KafkaProducer(bootstrap_servers='localhost:9092')
consumer = KafkaConsumer('topic_name', bootstrap_servers='localhost:9092')

def create_signature(data):
    sk = SigningKey.generate(curve=NIST256p)
    signature = sk.sign(data.encode())
    return base64.b64encode(signature)

for message in consumer:
    if message.key == b'data':
        data = redis_client.get("data")
        signature = create_signature(data)
        redis_client.set("signature", signature)
        producer.send('topic_name', key=b'signature_valid', value=b'signature_created')