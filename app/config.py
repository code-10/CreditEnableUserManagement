from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Base settings class"""
    PROJECT_NAME: str

    class Config:
        """Config Class"""
        case_sensitive = True

settings = Settings(PROJECT_NAME="CreditEnableUserManagement")