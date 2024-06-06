from app.services.utilities.rabbitmq_connector import connection_rabbitmq
from app.services.utilities.redis_connector import redis_connection
from app.services.utilities.signature import signature


CHAN=connection_rabbitmq()
def processing_message(body, chan=CHAN, r=redis_connection()):
    """Data processing for messages"""
    
    data = body.decode()
    sign = signature(data)
    r.set('signature', sign)
    chan.basic_consume(exchange='', routing_key='signature_queue', body=sign)
    
CHAN.basic_consume(queue='data_queue', on_message_callback=processing_message, auto_ack=True)
CHAN.start_consuming()
    