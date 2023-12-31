from enum import Enum

class InfoMessage(Enum):
    NO_USERS_FOUND = "No users found in the Database"
    USER_NOT_FOUND = "User not found"
    USER_ALREADY_EXISTS = "User with this email already exists"
    EMAIL_ALREADY_EXISTS = "User with this email already exists. Please choose a different email"
    USER_ADDED_SUCCESSFULLY = "User added successfully"
    USER_UPDATED_SUCCESSFULLY = "User updated successfully"
    USER_DELETED_SUCCESSFULLY = "User deleted successfully"