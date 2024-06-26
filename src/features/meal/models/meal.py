from typing import TYPE_CHECKING, Optional
from uuid import UUID

from advanced_alchemy import SQLAlchemyAsyncRepository, SQLAlchemyAsyncRepositoryService
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from features.meal.models.product import Product
    from features.user.models.user import User


class Meal(UUIDAuditBase):
    __tablename__ = 'meals'

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"), index=True)
    weight: Mapped[Optional[int]]
    user: Mapped["User"] = relationship(
        back_populates="meals",
        lazy="noload",
    )
    product: Mapped["Product"] = relationship(
        back_populates="meals",
        lazy="selectin",
    )


class MealRepository(SQLAlchemyAsyncRepository[Meal]):
    model_type = Meal


class MealService(SQLAlchemyAsyncRepositoryService[Meal]):
    repository_type = MealRepository
