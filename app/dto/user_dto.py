from sqlmodel import SQLModel, Field

class AddUser(SQLModel):
    email: str = Field(None, alias="email")
    first_name: str = Field(None, alias="first_name")
    last_name: str = Field(None, alias="last_name")
    gender: str = Field(None, alias="gender")
    password: str = Field(None, alias="password")

class UpdateUser(SQLModel):
    id: int = Field(None, alias="id")
    email: str = Field(None, alias="email")
    first_name: str = Field(None, alias="first_name")
    last_name: str = Field(None, alias="last_name")

class DeleteUser(SQLModel):
    id: int = Field(None, alias="id")
    