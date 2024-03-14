from typing import List, TYPE_CHECKING

from advanced_alchemy import SQLAlchemyAsyncRepository, SQLAlchemyAsyncRepositoryService
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

if TYPE_CHECKING:
    from models import Meal


class MealStore(UUIDAuditBase):
    __tablename__ = 'meal_stores'

    name: Mapped[str] = mapped_column(String(255))
    meals: Mapped[List["Meal"]] = relationship(back_populates="store")


class MealStoreRepository(SQLAlchemyAsyncRepository[MealStore]):
    model_type = MealStore


class MealStoreService(SQLAlchemyAsyncRepositoryService[MealStore]):
    repository_type = MealStoreRepository
