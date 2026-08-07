from fastapi import APIRouter, Depends
from app.models.user import User
from app.core.permissions import require_role


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/dashboard")
async def admin_dashboard(
    current_user: User = Depends(
        require_role("admin")
    )
):
    return {
        "message": "Welcome Admin",
        "user": current_user.email
    }