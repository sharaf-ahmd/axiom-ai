import pytest_asyncio

from app.database import SessionLocal


@pytest_asyncio.fixture
async def db_session():

    async with SessionLocal() as session:

        yield session