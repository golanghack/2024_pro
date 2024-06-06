import pika 
import os 

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')

def connection_rabbitmq():
    """Create connetion with rabbitmq"""
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel_to_rabbitmq = connection.channel()
    chan = channel_to_rabbitmq.queue_declare(queue='data_queue')
    return chan
    
    