from typing import Optional

from pydantic import EmailStr, BaseModel


from backend.schemas.order_schema import OrderRead


class CustomerRead(BaseModel):
    "This class is used as Response Model in Router"

    id: int
    email: str
    username: str
    orders: list[OrderRead]


class CustomerCreate(BaseModel):
    email: EmailStr
    username: str
    password: Optional[str] = "admin"  # ← Plain password from user

    def __str__(self):
        return self.email


class CustomerUpdate(BaseModel):
    email: EmailStr | None = None
    is_staff: bool
    is_active: bool
