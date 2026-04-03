from typing import Optional

from pydantic import EmailStr, BaseModel

from backend.models.customer import CustomBase


# https://fastapi.tiangolo.com/tutorial/sql-databases/#heropublic-the-public-data-model
class CustomerPublic(CustomBase):
    id: int  # ovevrride id from CustomBase


class CustomerCreate(BaseModel):
    email: EmailStr
    username: str
    password: Optional[str] = "admin"  # ← Plain password from user

    def __str__(self):
        return self.email


class CustomerUpdate(CustomBase):
    email: EmailStr | None = None
    is_staff: bool
    is_active: bool
