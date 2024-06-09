from django.http import HttpResponse
import redis
import random
import string

r = redis.Redis(host='redis', port=6379) # TODO -> outer in .env file

def generate_data_and_save(request: str) -> HttpResponse:
    # start a empty string 
    # after start added new sporadic data
    data = ''.join(random.choices(string.ascii_letters, k=200000))
    # save data in redis
    r.set('data', data)
    return HttpResponse("Data generated and saved in Redis")