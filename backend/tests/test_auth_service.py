import pytest
import uuid

from app.services.auth_service import AuthService
from app.schemas.auth import RegisterRequest, LoginRequest
from app.core.security import verify_password


@pytest.mark.asyncio
async def test_register_user(db_session):

    email = f"test_{uuid.uuid4()}@gmail.com"

    user_data = RegisterRequest(
        email=email,
        password="password123",
        full_name="Test User"
    )

    user = await AuthService.register(
        db_session,
        user_data
    )

    assert user.email == email
    assert user.full_name == "Test User"
    assert user.hashed_password != "password123"
    assert verify_password(
        "password123",
        user.hashed_password
    )


@pytest.mark.asyncio
async def test_login_user(db_session):

    email = f"login_{uuid.uuid4()}@gmail.com"

    register_data = RegisterRequest(
        email=email,
        password="password123",
        full_name="Login User"
    )

    await AuthService.register(
        db_session,
        register_data
    )


    login_data = LoginRequest(
        email=email,
        password="password123"
    )


    token = await AuthService.login(
        db_session,
        login_data
    )


    assert token is not None
    assert isinstance(token, dict)
    assert "access_token" in token
    assert "refresh_token" in token