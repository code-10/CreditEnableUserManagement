from datetime import datetime, timedelta
from app.tasks.email_tasks import send_confirmation_email
from fastapi import Depends
from sqlmodel import Session
from app.database import get_session
from app.repository import user_management_repository

def get_all_users(db_session: Session = Depends(get_session)):
    response = user_management_repository.get_all_users(db_session)
    if isinstance(response, str):
        return [{"response":response}]
    return response

def get_user(user_id, db_session: Session = Depends(get_session)):
    response = user_management_repository.get_user(user_id, db_session)
    if isinstance(response, str):
        return [{"response":response}]
    return response

def add_user(user, db_session: Session = Depends(get_session)):
    response = user_management_repository.add_user(user, db_session)
    if isinstance(response, str):
        return [{"response":response}]
    elif response is not None:
        send_confirmation_email.apply_async(queue='celery', eta=datetime.now() + timedelta(minutes=1), countdown=1)
        return response

def update_user(user, db_session: Session = Depends(get_session)):
    response = user_management_repository.update_user(user, db_session)
    if isinstance(response, str):
        return [{"response":response}]
    return response

def delete_user(user, db_session: Session = Depends(get_session)):
    response = user_management_repository.delete_user(user, db_session)
    if isinstance(response, str):
        return [{"response":response}]
    return response
