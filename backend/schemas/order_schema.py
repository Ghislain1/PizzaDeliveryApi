from typing import Optional
from pydantic import BaseModel
from enum import Enum


class PizzaSize(str, Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extra-large"


class OrderStatus(str, Enum):
    PENDING = "pending"
    IN_TRANSIT = "in-transit"
    DELIVERED = "delivered"


class OrderRead(BaseModel):
    """Order response model"""

    id: int
    quantity: int
    order_status: OrderStatus
    pizza_size: PizzaSize
    customer_id: Optional[int] = None

    class Config:
        from_attributes = True
