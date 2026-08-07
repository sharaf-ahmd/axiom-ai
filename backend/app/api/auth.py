from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

from app.schemas.auth import(
    RegisterRequest,
    LoginRequest, 
    TokenResponse,
    RefreshTokenRequest
)

from app.schemas.user import UserResponse
from app.services.auth_service import AuthService
from app.schemas.auth import LogoutRequest

router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)

@router.post("/register",response_model=UserResponse)
async def register(user_data:RegisterRequest, db:AsyncSession= Depends(get_db)):
    
        user = await AuthService.register(db,user_data)
        return user

@router.post("/login",response_model=TokenResponse)
async def login(credentials:LoginRequest, db:AsyncSession=Depends(get_db)):
    try:
        tokens = await AuthService.login(db,credentials)
        return {
            "access_token": tokens["access_token"],
            "refresh_token":tokens["refresh_token"],
            "token_type": "bearer"
        }
    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )

@router.post("/refresh")
async def refrsh(request:RefreshTokenRequest, db:AsyncSession = Depends(get_db)):
    tokens = await AuthService.refresh(
        db,
        request.refresh_token
    )
    return {
         "access_token": tokens["access_token"],
         "refresh_token": tokens["refresh_token"],
         "token_type": "bearer"
    }

@router.post("/logout")
async def logout(request: LogoutRequest, db: AsyncSession = Depends(get_db)):

     await AuthService.logout(db,request.refresh_token)
     return {"message":"Successfully logged out"}

