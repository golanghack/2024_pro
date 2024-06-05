import aioredis
import os 

async def redis_connector():
    """Return redis connector object"""
    
    redis = await aioredis.create_redis_pool(os.getenv('REDIS_URL'))
    return redis