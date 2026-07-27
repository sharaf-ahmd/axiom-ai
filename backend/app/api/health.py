from fastapi import APIRouter
from app.services.redis import redis_health
from app.services.database import database_health

router=APIRouter()

@router.get("/health")
async def health():

    return {

        "status":"healthy",
        "services":{
            "database":
            await database_health(),

            "redis":
            await redis_health()
            
        }
    }