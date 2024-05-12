from fastapi import APIRouter
from src.model.create import Create
import src.fake.create as service 

router = APIRouter(prefix='/create')

@router.get('/')
def get_all() -> list[Create]:
    return service.get_all()

@router.get('/{name}')
def get_one(name) -> Create:
    return service.get_one(name)

@router.post('/')
def create(create: Create) -> Create:
    return service.create(create)

@router.patch('/')
def modify(create: Create) -> Create:
    return service.modify(create)

@router.put('/')
def replace(create: Create) -> Create:
    return service.replace(create)

@router.delete('/')
def delete(name: str):
    return service.delete(name)