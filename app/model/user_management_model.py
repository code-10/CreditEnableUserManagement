from typing import Optional
from datetime import datetime
import os
from sqlmodel import Field, SQLModel, Column, VARCHAR,INT
from dotenv import load_dotenv

load_dotenv()

class User(SQLModel, table=True):
    """
        Creating database Structure for User table
    """
    __tablename__ = 'user'

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(sa_column=Column("first_name", VARCHAR(54), nullable=False))
    last_name: str = Field(sa_column=Column("last_name", VARCHAR(54), nullable=True))
    gender: str = Field(sa_column=Column("gender", VARCHAR(54), nullable=True))
    email: str = Field(sa_column=Column("email", VARCHAR(150), unique=True, nullable=False))
    password: str = Field(sa_column=Column("password", VARCHAR(256), nullable=False))