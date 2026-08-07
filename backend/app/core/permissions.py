from fastapi import Depends, HTTPException, status
from app.models.user import User
from app.core.dependencies import get_current_user

def require_role(required_role: str):

    async def role_checker(current_user: User =Depends(get_current_user)):
        if current_user.role !=required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )
        return current_user
    return role_checker