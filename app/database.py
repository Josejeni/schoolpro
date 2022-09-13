from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

engine=create_engine(f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:5432/{settings.database_name}')
Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()