from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec 
from app.utilities.connector_redis import redis_connector as conn 

PRIVATE_KEY = ec.generate_private_key(ec.SECP256R1())

async def signature():
    """Create signature"""
    # connection with redis
    redis = conn()
    # response data
    data = redis.get('data')
    # serializer
    serializer_pk = PRIVATE_KEY.private_bytes(encoding=serialization.Encoding.PEM, 
                                              format=serialization.PrivateFormat.TraditionalOpenSSL,
                                              encryption_algorithm=serialization.NoEncryption())
    # create signature
    signature = PRIVATE_KEY.sign(data, ec.ECDSA(hashes.SHA256()))
    # set in 
    await redis.set('signature', signature)
    return {'message': 'Signature saved in Redis'}