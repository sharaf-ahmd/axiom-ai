import pytest

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.auth_service import AuthService
from app.schemas.auth import RegisterRequest

@pytest.mark.asyncio
async def test_register_user(db_session):

    user_data = RegisterRequest(
        email="testuser@gmail.com",
        password="password123",
        full_name="Test User"
    )


    user = await AuthService.register(
        db_session,
        user_data
    )


    assert user.email == "testuser@gmail.com"

    assert user.full_name == "Test User"

    assert user.hashed_password != "password123"