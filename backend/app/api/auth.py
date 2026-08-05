from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

from app.schemas.auth import(
    RegisterRequest,
    LoginRequest, 
    TokenResponse
)

from app.schemas.user import UserResponse
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)

@router.post("/register",response_model=UserResponse)
async def register(user_data:RegisterRequest, db:AsyncSession= Depends(get_db)):
    try:
        user = await AuthService.register(db,user_data)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.post("/login",response_model=TokenResponse)
async def login(credentials:LoginRequest, db:AsyncSession=Depends(get_db)):
    try:
        token = await AuthService.login(db,credentials)
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )