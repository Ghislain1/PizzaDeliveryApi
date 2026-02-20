from typing import Optional

from pydantic import EmailStr

from app.models.customer import CustomBase


# https://fastapi.tiangolo.com/tutorial/sql-databases/#heropublic-the-public-data-model
class CustomerPublic(CustomBase):
    id: int  # ovevrride id from CustomBase


class CustomerCreate(CustomBase):
    email: EmailStr
    password: str  # ← Plain password from user
    is_staff: Optional[bool] = False  # best practice
    is_active: Optional[bool] = True  # best practice


class CustomerUpdate(CustomBase):
    email: EmailStr | None = None
    is_staff: bool
    is_active: bool
