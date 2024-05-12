from pydantic import BaseModel

class Create(BaseModel):
    name: str 
    country: str 
    area: str 
    desc: str 
    aka: str 