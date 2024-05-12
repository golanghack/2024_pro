from fastapi import APIRouter
from src.model.explorer import Explorer
import src.fake.explorer as service 

router = APIRouter(prefix='/explorer')

@router.get('/')
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get('/{name}')
def get_one(name) -> Explorer | None:
    return service.get_one(name)

@router.post('/')
def create(exp: Explorer) -> Explorer:
    return service.create(exp)

@router.patch('/')
def modify(exp: Explorer) -> Explorer:
    return service.modify(exp)

@router.put('/')
def replace(exp: Explorer) -> Explorer:
    return service.replace(exp)

@router.delete('/{name}')
def delete(name: str):
    return None