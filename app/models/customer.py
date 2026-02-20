from __future__ import annotations
from typing import Optional, List
from pydantic import EmailStr


from sqlmodel import Field, Relationship, SQLModel

from app.models.order import Order


# All fields that are shared by models
class CustomBase(SQLModel):
    # Colunm Name in table
    username: Optional[str] = Field(default="unknow name ", unique=True, max_length=155)


# This is a table model not a data model ( see schema)
class Customer(CustomBase, table=True):
    # PK column in the table
    id: Optional[int] = Field(default=None, primary_key=True)

    # Column email in sqlModel with EmailStr validataion
    email: EmailStr = Field(
        sa_column=Field(sa_type=str, max_length=255),
        max_length=255,
    )

    # Best Pratice  to store password as hashed string
    hashed_password: str = Field(unique=True, nullable=False)
    is_staff: Optional[bool] = Field(default=False)
    is_active: Optional[bool] = Field(default=False)

    # Relation :  one cutomer -->  many orders *** Pylance provides Error  due to Order why?****
    orders: List[Order] = Relationship(back_populates="customer")

    def __repr__(self):
        return f"<User {self.username} - {self.email}"
