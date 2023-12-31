"""
    common json response structure
"""
from sqlmodel import SQLModel, Field

class Response(SQLModel):
    """
        function for constructing schema
    """
    message: str = Field(None, alias="message")
    status: str = Field(None, alias="status")
    data: list[dict] = Field(None, alias="data")

def create_response(message:str,status:str,data:list[dict]=None):
    """
        function for mapping the response
    """
    final_response = Response()
    final_response.message = message
    final_response.status = status
    final_response.data = data
    return final_response
