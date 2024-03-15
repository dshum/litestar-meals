from typing import List, TYPE_CHECKING

from advanced_alchemy import SQLAlchemyAsyncRepository, SQLAlchemyAsyncRepositoryService
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

if TYPE_CHECKING:
    from models import Meal


class MealBrand(UUIDAuditBase):
    __tablename__ = 'meal_brands'

    name: Mapped[str] = mapped_column(String(255), unique=True)
    meals: Mapped[List["Meal"]] = relationship(back_populates="brand")


class MealBrandRepository(SQLAlchemyAsyncRepository[MealBrand]):
    model_type = MealBrand


class MealBrandService(SQLAlchemyAsyncRepositoryService[MealBrand]):
    repository_type = MealBrandRepository
