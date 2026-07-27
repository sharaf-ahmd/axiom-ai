from sqlalchemy import text
from app.database import engine


async def database_health():

    try:
        async with engine.connect() as conn:
            await conn.execute(
                text("SELECT 1")
            )
        return True
    except Exception:

        return False    