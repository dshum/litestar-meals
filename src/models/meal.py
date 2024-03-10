from decimal import Decimal
from enum import Enum
from typing import List, TYPE_CHECKING
from uuid import UUID

from advanced_alchemy import SQLAlchemyAsyncRepository, SQLAlchemyAsyncRepositoryService
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import User, UserMeal


class Store(str, Enum):
    OZON = "Ozon"
    VKUSVILL = "Vkusvill"
    VARIOUS = "Various"


class Meal(UUIDAuditBase):
    __tablename__ = 'meals'

    name: Mapped[str] = mapped_column(String(1000))
    store: Mapped[Store]
    weight: Mapped[int | None] = mapped_column(nullable=True)
    calories: Mapped[Decimal]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    creator: Mapped["User"] = relationship(
        foreign_keys=[user_id],
        back_populates="created_meals",
    )
    users: Mapped[List["UserMeal"]] = relationship(back_populates="meal")


class MealRepository(SQLAlchemyAsyncRepository[Meal]):
    model_type = Meal


class MealService(SQLAlchemyAsyncRepositoryService[Meal]):
    repository_type = MealRepository
