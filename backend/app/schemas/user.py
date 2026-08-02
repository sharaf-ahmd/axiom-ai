import uuid
from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str | None
    is_active: bool
    class config:
        from_attribute = True