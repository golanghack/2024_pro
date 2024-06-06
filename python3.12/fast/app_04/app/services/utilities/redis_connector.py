import redis 
import os 

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))

def redis_connection(host: str=REDIS_HOST, port: int=REDIS_PORT, db: int=0):
    """Create connection with redis"""
    
    r = redis.Redis(host=host, port=port, db=db)
    return r 

