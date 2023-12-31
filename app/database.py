"""Database configuration"""
import os
import urllib

import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker
from app.database_config import DatabaseConfig
from sqlmodel import Session

load_dotenv()

config = DatabaseConfig(
    DB_NAME=os.getenv("DB_NAME"),
    DB_HOST=os.getenv("DB_HOST"),
    DB_USERNAME=os.getenv("DB_USERNAME"),
    DB_PASSWORD=os.getenv("DB_PASSWORD"),
    LOG_DB_HOST=os.getenv("LOG_DB_HOST"),
    LOG_DB_NAME=os.getenv("LOG_DB_NAME"),
    LOG_DB_USERNAME=os.getenv("LOG_DB_USERNAME"),
    LOG_DB_PASSWORD=os.getenv("LOG_DB_PASSWORD"),
)

def get_engine(**db_config):
    """Get Engine method"""
    connection_url = sqlalchemy.engine.URL.create(
        "mysql+pymysql",
        username=db_config['username'],
        password=db_config['password'],
        host=db_config['host'],
        database=db_config['database'],
        port=3306
    )
    
    engine = sqlalchemy.create_engine(connection_url).execution_options(
        isolation_level="AUTOCOMMIT"
    )
    return engine

engine = get_engine(username=config.DB_USERNAME,
password=config.DB_PASSWORD,
host=config.DB_HOST,
database=config.DB_NAME)

@as_declarative()
class Base:
    """Base class"""
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


def get_session():
    """Get session method"""
    with Session(engine) as session:
        yield session
