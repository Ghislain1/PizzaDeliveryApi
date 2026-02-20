from app.db.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship

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


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), default="SMALL")

    # relation
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="order")

    def __repr__(self):
        return f"<Order {self.id}"
