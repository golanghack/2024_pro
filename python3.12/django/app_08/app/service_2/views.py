from django.http import HttpResponse
import redis
import ecdsa
import base64

r = redis.Redis(host='redis', port=6379) # TODO -> added in .env file

def create_signature(data: str) -> str:
    """Created full signature for data and encoding"""
    
    # genrated
    sk = ecdsa.SigningKey.generate()
    # encoding
    signature = sk.sign(data.encode())
    return base64.b64encode(signature)

def process_data(request: str) -> HttpResponse:
    """Creation and saving a signature in redis """
    
    # from request object data direction
    data = r.get('data')
    # creating a new signature
    signature = create_signature(data)
    # save signature in redis
    r.set('signature', signature)
    return HttpResponse("Signature created and saved in Redis")

def verify_signature(request: str) -> HttpResponse:
    """Verification for signature from redis"""
    
    # get data from reis object
    data = r.get('data')
    # encoding data signature
    signature = base64.b64decode(r.get('signature'))
    # genereted
    sk = ecdsa.SigningKey.generate()
    # verification
    vk = ecdsa.VerifyingKey.from_public_key(sk.get_verifying_key(), curve=ecdsa.NIST256p)
    # conditions for verification
    if vk.verify(signature, data):
        return HttpResponse("Signature is valid")
    else:
        return HttpResponse("Signature is invalid")