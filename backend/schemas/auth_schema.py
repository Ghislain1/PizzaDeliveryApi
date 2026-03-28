from pydantic import BaseModel, EmailStr
from typing import Optional, Annotated


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: EmailStr
    password: str
    is_staff: Annotated[bool, None]
    is_active: Annotated[bool, None]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "john@dpe.com",
                "is_staff": False,
                "is_active": True,
            }
        }
