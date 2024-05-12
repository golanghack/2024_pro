from src.model.explorer import Explorer

_explorers = [
    Explorer(name='One One', 
             country='FR', 
             desc='Super',
             ),
    Explorer(name='Two Two', 
             country='USA',
             desc='A new ',),
]

def get_all() -> list[Explorer]:
    """Return all explorers"""
    
    return _explorers

def get_one(name: str) -> Explorer | None:
    """Return explorer on name"""
    
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None 

def create(explorer: Explorer) -> Explorer:
    """Add"""
    
    return explorer

def modify(explorer: Explorer) -> Explorer:
    """Modification"""
    
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """Completely replace explorer"""
    
    return explorer

def delete(name: str) -> bool:
    """Delete explorer."""
    
    return None