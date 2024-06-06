from ecdsa import SigningKey, NIST256p
import base64

def signature(data):
    """Create signature"""
    
    signature_key = SigningKey.generate(curve=NIST256p)
    sign = signature_key.sign(data.encode())
    return base64.b64encode(sign)

