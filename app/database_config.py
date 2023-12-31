from pydantic import BaseModel

class DatabaseConfig(BaseModel):
    DB_NAME: str
    DB_HOST: str
    DB_USERNAME: str
    DB_PASSWORD: str

    LOG_DB_HOST: str
    LOG_DB_NAME: str
    LOG_DB_USERNAME: str
    LOG_DB_PASSWORD: str
    