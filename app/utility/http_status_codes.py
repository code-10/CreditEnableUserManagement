"""
    Enums for HTTP Status CodesS
"""
from enum import Enum

class HttpStatusCodes():
    """
        Nested Classes for StatusCodes response and StatusCodesDesription response
    """
    def __init__(self):
        pass
    
    class StatusCodes(Enum):
        """
        Enums for StatusCodes
        """
        SUCCESS_OK_200 = '200'
        BAD_REQUEST_400 = '400'
        UNAUTHORIZED_401 = '401'
        FORBIDDEN_403 = '403'
        NOT_FOUND_404 = '404'
        INTERNAL_SERVER_ERROR_500 = '500'
        NOT_IMPLEMENTED_501 = '501'

    class StatusCodesDescription(Enum):
        """
        Enums for StatusCodesDescription
        """
        SUCCESS_OK_200 = 'Ok'
        BAD_REQUEST_400 = 'Bad Request'
        UNAUTHORIZED_401 = 'Unauthorized'
        FORBIDDEN_403 = 'Forbidden'
        NOT_FOUND_404 = 'Not Found'
        INTERNAL_SERVER_ERROR_500 = 'Internal Server Error'
        NOT_IMPLEMENTED_501 = 'Not Implemented'

