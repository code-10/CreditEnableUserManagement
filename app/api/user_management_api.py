from datetime import datetime, timedelta
from app import celery_config
from app.tasks.email_tasks import send_confirmation_email
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.dto.user_dto import AddUser, DeleteUser, UpdateUser
from app.database import get_session
from app.utility import response as res
from app.utility.http_status_codes import HttpStatusCodes
from app.service import user_management_service
from motor.motor_asyncio import AsyncIOMotorClient
from app.utility.logging import get_mongo_client, loggod, LoggingLevels

router = APIRouter()


@router.get("/user_management/get_all_users")
async def get_all_users(db_session: Session = Depends(get_session), client: AsyncIOMotorClient = Depends(get_mongo_client)):
    loggod(LoggingLevels.INFO, "Entered Method get_all_users", client)
    response = user_management_service.get_all_users(db_session)
    return res.create_response(
        HttpStatusCodes.StatusCodesDescription.SUCCESS_OK_200.value,
        HttpStatusCodes.StatusCodes.SUCCESS_OK_200.value,
        response)

@router.get("/user_management/get_user/{user_id}")
async def get_user(user_id: int, db_session: Session = Depends(get_session)):
    response = user_management_service.get_user(user_id, db_session)
    return res.create_response(
        HttpStatusCodes.StatusCodesDescription.SUCCESS_OK_200.value,
        HttpStatusCodes.StatusCodes.SUCCESS_OK_200.value,
        response)

@router.post("/user_management/add_user")
async def add_user(user: AddUser, db_session: Session = Depends(get_session)):
    response = user_management_service.add_user(user, db_session)
    return res.create_response(
        HttpStatusCodes.StatusCodesDescription.SUCCESS_OK_200.value,
        HttpStatusCodes.StatusCodes.SUCCESS_OK_200.value,
        response)

@router.put("/user_management/update_user")
async def update_user(user: UpdateUser, db_session: Session = Depends(get_session)):
    response = user_management_service.update_user(user, db_session)
    return res.create_response(
        HttpStatusCodes.StatusCodesDescription.SUCCESS_OK_200.value,
        HttpStatusCodes.StatusCodes.SUCCESS_OK_200.value,
        response)

@router.delete("/user_management/delete_user")
async def delete_user(user: DeleteUser, db_session: Session = Depends(get_session)):
    response = user_management_service.delete_user(user, db_session)
    return res.create_response(
        HttpStatusCodes.StatusCodesDescription.SUCCESS_OK_200.value,
        HttpStatusCodes.StatusCodes.SUCCESS_OK_200.value,
        response)


