from app.database_config import DatabaseConfig
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
import logging
from datetime import datetime
from dotenv import load_dotenv
import os

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

async def get_mongo_client():
    try:
        host = config.LOG_DB_HOST
        username = config.LOG_DB_USERNAME
        password = config.LOG_DB_PASSWORD
        database_name = config.LOG_DB_NAME

        connection_url = f"mongodb+srv://{username}:{password}@{host}/{database_name}?retryWrites=true&w=majority"    
        mongo_client = AsyncIOMotorClient(connection_url)
        yield mongo_client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

def loggod(level, message, mongo_client: AsyncIOMotorClient = Depends(get_mongo_client)):
    if mongo_client is not None:
        try:
            log_data = {
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'level': level,
                'message': message,
            }

            log_data = {key: value for key, value in log_data.items() if isinstance(value, (int, float, str, bool))}

            mongo_client.creditEnableDb.logs.insert_one(log_data)
            return log_data
        except Exception as e:
            print(f"Error inserting log data into MongoDB: {e}")
    else:
        print("MongoDB client is not available.")

from enum import Enum

class LoggingLevels(Enum):
    """
    Enums for Logging Levels
    """
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

# @app.on_event("shutdown")
# async def close_mongo_client(client: AsyncIOMotorClient = Depends(get_mongo_client)):
#     client.close()
    
