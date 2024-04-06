from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from features.meal.models.brand import Brand
    from features.meal.models.meal import Meal
    from features.meal.models.store import Store
    from features.user.models.user import User


class Product(UUIDAuditBase):
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(1000))
    weight: Mapped[int | None] = mapped_column(nullable=True)
    calories: Mapped[Decimal]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    store_id: Mapped[UUID | None] = mapped_column(ForeignKey("stores.id"), index=True)
    brand_id: Mapped[UUID | None] = mapped_column(ForeignKey("brands.id"), index=True)
    user: Mapped["User"] = relationship(
        foreign_keys=[user_id],
        back_populates="products",
        lazy="noload",
    )
    store: Mapped["Store"] = relationship(
        foreign_keys=[store_id],
        back_populates="products",
        lazy="selectin",
    )
    brand: Mapped["Brand"] = relationship(
        foreign_keys=[brand_id],
        back_populates="products",
        lazy="selectin",
    )
    meals: Mapped["Meal"] = relationship(
        back_populates="product",
        lazy="selectin",
    )

    __table_args__ = (UniqueConstraint("name", "user_id"),)
