from typing import TYPE_CHECKING
from uuid import UUID

from advanced_alchemy import SQLAlchemyAsyncRepository, SQLAlchemyAsyncRepositoryService
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import User, Meal


class UserMeal(UUIDAuditBase):
    __tablename__ = 'user_meals'

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)
    meal_id: Mapped[UUID] = mapped_column(ForeignKey("meals.id"), primary_key=True)
    weight: Mapped[int]
    user: Mapped["User"] = relationship(back_populates="meals")
    meal: Mapped["Meal"] = relationship(back_populates="users")


class UserMealRepository(SQLAlchemyAsyncRepository[UserMeal]):
    model_type = UserMeal


class UserMealService(SQLAlchemyAsyncRepositoryService[UserMeal]):
    repository_type = UserMealRepository
