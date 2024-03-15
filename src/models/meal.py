from decimal import Decimal
from typing import List, TYPE_CHECKING
from uuid import UUID

from advanced_alchemy import SQLAlchemyAsyncRepository, SQLAlchemyAsyncRepositoryService
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import User, UserMeal, MealStore, MealBrand


class Meal(UUIDAuditBase):
    __tablename__ = 'meals'

    name: Mapped[str] = mapped_column(String(1000), unique=True)
    weight: Mapped[int | None] = mapped_column(nullable=True)
    calories: Mapped[Decimal]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    meal_store_id: Mapped[UUID] = mapped_column(ForeignKey("meal_stores.id"), index=True)
    meal_brand_id: Mapped[UUID] = mapped_column(ForeignKey("meal_brands.id"), index=True)
    creator: Mapped["User"] = relationship(
        foreign_keys=[user_id],
        back_populates="created_meals",
        lazy="noload",
    )
    store: Mapped["MealStore"] = relationship(
        foreign_keys=[meal_store_id],
        back_populates="meals",
        lazy="selectin",
    )
    brand: Mapped["MealBrand"] = relationship(
        foreign_keys=[meal_brand_id],
        back_populates="meals",
        lazy="selectin",
    )
    users: Mapped[List["UserMeal"]] = relationship(back_populates="meal")


class MealRepository(SQLAlchemyAsyncRepository[Meal]):
    model_type = Meal


class MealService(SQLAlchemyAsyncRepositoryService[Meal]):
    repository_type = MealRepository
