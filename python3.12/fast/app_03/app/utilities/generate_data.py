import random 

def generate_data():
    """Generate sporadic data for redis"""
    
    data = bytearray(random.getrandbits(8) for _ in range(25600))
    return data 