from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from uuid import UUID

from advanced_alchemy import SQLAlchemyAsyncRepository, SQLAlchemyAsyncRepositoryService
from advanced_alchemy.base import UUIDAuditBase
from litestar.dto import dto_field
from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from features.meal.models.brand import Brand
from features.meal.models.store import Store

if TYPE_CHECKING:
    from features.meal.models.meal import Meal
    from features.user.models.user import User


class Product(UUIDAuditBase):
    __tablename__ = 'products'
    __table_args__ = (UniqueConstraint("name", "user_id"),)

    name: Mapped[str] = mapped_column(String(1000))
    weight: Mapped[int | None] = mapped_column(nullable=True)
    calories: Mapped[Decimal]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    brand_id: Mapped[UUID | None] = mapped_column(ForeignKey("brands.id"), default=None, index=True)
    store_id: Mapped[UUID | None] = mapped_column(ForeignKey("stores.id"), default=None, index=True)
    user: Mapped["User"] = relationship(
        foreign_keys=[user_id],
        back_populates="products",
        lazy="noload",
    )
    brand: Mapped[Optional[Brand]] = relationship(
        foreign_keys=[brand_id],
        back_populates="products",
        lazy="selectin",
    )
    store: Mapped[Optional[Store]] = relationship(
        foreign_keys=[store_id],
        back_populates="products",
        lazy="selectin",
    )
    meals: Mapped["Meal"] = relationship(
        back_populates="product",
        lazy="selectin",
    )


class ProductRepository(SQLAlchemyAsyncRepository[Product]):
    model_type = Product


class ProductService(SQLAlchemyAsyncRepositoryService[Product]):
    repository_type = ProductRepository
