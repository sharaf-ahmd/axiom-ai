from fastapi import Request
from fastapi.responses import JSONResponse

async def global_exception_handler(request:Request,exc:Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error":"Internal Server error"
        }
    )


class AppException(Exception):
    pass

class EmailAlreadyExists(AppException):
    def __init__(self):
        self.message = "Email already registered"


class InvalidCredentials(AppException):
    def __init__(self):
        self.message = "Invalid email or password"


class UserNotFound(AppException):
    def __init__(self):
        self.message = "User not found"

async def app_exception_handler(
    request: Request,
    exc: AppException
):

    return JSONResponse(
        status_code=400,
        content={
            "error": exc.message
        }
    )        