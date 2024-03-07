from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.core.config import settings

SQL_ALCHEMY_DB_URL = settings.DATABASE_URL
print('DB Url -> ', SQL_ALCHEMY_DB_URL)
engine = create_engine(SQL_ALCHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)