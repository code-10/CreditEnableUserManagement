from app.middleware.logging_middleware import RequestResponseLoggingMiddleware
from fastapi import FastAPI
from app.api import user_management_api
from app.config import settings
from app.database import engine
from app.model import user_management_model
from sqlmodel import SQLModel
from celery import Celery
from app.celery_config import celery as celery_app


def get_application():
    """
    function to setup fastapi application
    """
    _app = FastAPI(
        title=settings.PROJECT_NAME
    )

    return _app

app = get_application()

#For Creating tables in the database
user_management_model.SQLModel.metadata.create_all(engine)

app.include_router(user_management_api.router, prefix="/api",tags=['User Management'])

app.celery_app = celery_app

app.add_middleware(RequestResponseLoggingMiddleware)

