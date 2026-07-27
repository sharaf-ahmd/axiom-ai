import redis.asyncio as redis
from app.config import settings

redis_client=redis.from_url(
    settings.REDIS_URL,
    decode_response=True
)

async def redis_health():
    return await redis_client.ping()