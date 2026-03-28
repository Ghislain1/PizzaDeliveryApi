from typing import Optional, TYPE_CHECKING
from enum import Enum as PyEnum

if TYPE_CHECKING:
    from backend.models.customer import Customer  # adjust import path

# from enum import Enum
from sqlmodel import (
    Column,
    Relationship,
    Enum,  # ************ Right Emun not from python builtin enum***********
    Field,
)

from backend.models.base import EntityBase


ORDER_STATUSES = (
    ("PENDING", "pending"),
    ("IN_TRANSIT", "in-transit"),
    ("DELIVERED", "delivered"),
)
PIZZA_SIZES = (
    ("SMALL", "small"),
    ("MEDIUM", "medium"),
    ("LARGE", "large"),
    ("EXTRA_LARGE", "extra-large"),
)


# enum for size of pizza
class PizzaSize(str, PyEnum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extra-large"


# Enum for order status
class OrderStatus(str, PyEnum):
    PENDING = "pending"
    IN_TRANSIT = "in-transit"
    DELIVERED = "delivered"


class Order(EntityBase, table=True):
    # id: Optional[int] = Field(default=None, primary_key=True)
    quantity: Optional[int] = Field(default=1, nullable=False)
    # SQLModel Attribut with enum Column
    order_status: OrderStatus = Field(
        sa_column=Column(Enum(OrderStatus, name="order_status_enum")),
        default=OrderStatus.PENDING,
    )
    # Defining a Column as Enum
    pizza_size: PizzaSize = Field(
        sa_column=Column(Enum(PizzaSize, name="pizza_size_enum")),
        default=PizzaSize.SMALL,
    )

    # relation: FK column
    custom_id: Optional[int] = Field(default=None, foreign_key="customer.id")

    # relation: many orders -> one customer **** # use string "Customer", no import of Order here ***
    customer: Optional["Customer"] = Relationship(back_populates="orders")

    def __repr__(self):
        return f"<Order {self.id}"
