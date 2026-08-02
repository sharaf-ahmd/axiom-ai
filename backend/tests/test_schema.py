from app.schemas.auth import RegisterRequest

def test_register_schema():

    user = RegisterRequest(
        email="test@example.com",
        password="password123",
        full_name="Test User"
    )

    assert user.email == "test@example.com"

    assert user.full_name == "Test User"