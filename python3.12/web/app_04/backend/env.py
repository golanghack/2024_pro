from alembic import context 
from backend.core.config import settings
from backend.db import Base

config = context.config 
config.set_main_option('sqlalchemy.url', settings.DATABASE_URL)
target_metadata = Base.metadata 