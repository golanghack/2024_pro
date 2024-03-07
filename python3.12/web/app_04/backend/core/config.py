import os 
from dotenv import load_dotenv 
from pathlib import Path
env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = 'Hola'
    PROJECT_VERSION: str = '1.0.0'
    
    # db 
    POSTGRES_USER=os.getenv('POSTGRES_USER', 'fastapi1')
    POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD', 'x326y457z')
    POSTGRES_SERVER=os.getenv('POSTGRES_SERVER', 'localhost')
    POSTGRES_PORT=os.getenv('POSTGRES_PORT', 5432)
    POSTGRES_DB=os.getenv('POSTGRES_DB', 'fastapi1db')
    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'
    
settings = Settings()