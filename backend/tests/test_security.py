from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token
)

def test_password_hash():

    password = "test123"
    hashed=hash_password(password)

    assert password != hashed

    assert verify_password(password,hashed)

def test_jwt():

    token = create_access_token({"user_id":"123"})

    payload= decode_access_token(token)

    assert payload["user_id" ]== "123"