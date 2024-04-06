from typing import TYPE_CHECKING
from uuid import UUID

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from features.meal.models.product import Product
    from features.user.models.user import User


class Meal(UUIDAuditBase):
    __tablename__ = 'meals'

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"), primary_key=True)
    weight: Mapped[int]
    user: Mapped["User"] = relationship(
        back_populates="meals",
        lazy="selectin",
    )
    product: Mapped["Product"] = relationship(
        back_populates="meals",
        lazy="selectin",
    )
