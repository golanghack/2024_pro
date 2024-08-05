from kafka import KafkaConsumer, KafkaProducer
import json
from django.conf import settings

class KafkaHandler:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.consumer = KafkaConsumer(
            'food',
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='food_group',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
    
    def produce(self, topic, value):
        self.producer.send(topic, value)

    def consume(self):
        for message in self.consumer:
            yield message.value