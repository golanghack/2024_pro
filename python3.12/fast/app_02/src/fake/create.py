from src.model.create import Create

_creates = [
    Create(name='One', 
           aka='Snowman',
           country='CA',
           area='Forest',
           desc='Forest man'),
    Create(name='Two',
           aka='Foodman',
           country='USA',
           area='Foods',
           desc='Food man'),
]

def get_all() -> list[Create]:
    """Get all mans"""
    
    return _creates

def get_one(name: str) -> Create | None:
    """Return one man"""
    
    for _create in _creates:
        if _create.name == name:
            return _create 
    return None 

def create(create: Create) -> Create:
    """Create a man"""
    
    return create

def modify(create: Create) -> Create:
    return create

def replace(create: Create) -> Create:
    return create

def delete(name: str) -> bool:
    return None 