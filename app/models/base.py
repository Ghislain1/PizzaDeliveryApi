from __future__ import annotations
from typing import Generic, Optional, TypeVar, List
from sqlalchemy.orm import declared_attr
from sqlmodel import SQLModel, Field, Relationship

# Generic Base Class
T = TypeVar("T")


class EntityBase(SQLModel):
    __abstract__ = True

    id: Optional[int] = Field(default=None, primary_key=True)

    # Generic relationship - override in subclasses
    # related_items: List[T] = Relationship(back_populates="entity")
