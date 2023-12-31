from fastapi import Depends
from sqlmodel import Session
from sqlalchemy import select 
from app.database import get_session
from app.model.user_management_model import User
from app.utility import convert_results, password_hasher
from app.utility.info_messages import InfoMessage

def get_all_users(db_session: Session = Depends(get_session)):
    statement = select(User.email, User.first_name, User.last_name)
    results = db_session.exec(statement)
    if results is not None:
        response = convert_results.convertPydanticToJson(results)
        return response
    else:
        return InfoMessage.NO_USERS_FOUND.value

def get_user(user_id, db_session: Session = Depends(get_session)):
    statement = select(User.email, User.first_name, User.last_name).where(User.id == user_id)
    results = db_session.exec(statement)
    if results is not None:
        response = convert_results.convertPydanticToJson(results)
        return response
    else:
        return InfoMessage.USER_NOT_FOUND.value

def add_user(user, db_session: Session = Depends(get_session)):
    is_email_already_exists = is_email_already_exists(user.email, db_session)
    if is_email_already_exists is None:
        new_user = User(email = user.email, first_name = user.first_name, gender = user.gender,
                        last_name = user.last_name, password = user.password)
        db_session.add(new_user)
        db_session.commit()
        response = InfoMessage.USER_ADDED_SUCCESSFULLY.value
        return response
    else:
        return InfoMessage.USER_ALREADY_EXISTS.value

def update_user(user, db_session: Session = Depends(get_session)):
    existing_user = db_session.get(User, user.id)
    if existing_user is not None:
        is_email = is_email_already_exists(user.email, db_session)
        if is_email is not None:
            return "user with this email already exists please choose a different email"
        
        if user.email is not None:
            existing_user.email = user.email
        if user.first_name is not None:
            existing_user.first_name = user.first_name
        if user.last_name is not None:
            existing_user.last_name = user.last_name
        db_session.commit()
        return InfoMessage.USER_UPDATED_SUCCESSFULLY.value
    else:
        return InfoMessage.USER_NOT_FOUND.value
    
def delete_user(user, db_session: Session = Depends(get_session)):
    existing_user = db_session.get(User, user.id)
    if existing_user is not None:
        db_session.delete(existing_user)
        db_session.commit()
        return InfoMessage.USER_DELETED_SUCCESSFULLY.value
    else:
        return InfoMessage.USER_NOT_FOUND.value

def is_email_already_exists(email, db_session: Session = Depends(get_session)):
    statement = select(User).where(User.email == email)
    is_email = db_session.exec(statement).first()
    return is_email
