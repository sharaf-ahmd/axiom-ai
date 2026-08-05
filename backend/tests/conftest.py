import pytest_asyncio

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from app.models.base import Base


TEST_DATABASE_URL = (
    "postgresql+asyncpg://axiom:password@localhost:5432/axiom_test"
)


@pytest_asyncio.fixture
async def db_session():

    engine = create_async_engine(
        TEST_DATABASE_URL,
        echo=False
    )

    TestingSessionLocal = async_sessionmaker(
        engine,
        expire_on_commit=False
    )


    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )


    async with TestingSessionLocal() as session:

        yield session


    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.drop_all
        )


    await engine.dispose()