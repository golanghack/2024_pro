from django.http import JsonResponse
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

def process_data(request: str) -> JsonResponse:
    """Creation and saving a signature in redis """
    
    # from request object data direction
    data = r.get('data')
    string_data = str(data)
    # creating a new signature
    signature = create_signature(string_data)
    # save signature in redis
    r.set('signature', signature)
    return JsonResponse({'message':"Signature created and saved in Redis"})

def verify_signature(request: str) -> JsonResponse:
    """Verification for signature from redis"""
    
    # get data from reis object
    data = bytes(str(r.get('data')), 'ascii')
    
    # genereted
    sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
    # verification
    vk = sk.verifying_key
    # signature
    signature = sk.sign(r.get('signature'))
    # conditions for verification
    if vk.verify(signature, data):
        return JsonResponse({'message': 'Signature is valid'})
    else:
        return JsonResponse({'message': 'Error! Signature is not valid'})