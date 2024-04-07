from typing import List, TYPE_CHECKING

from advanced_alchemy import SQLAlchemyAsyncRepository, SQLAlchemyAsyncRepositoryService
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

if TYPE_CHECKING:
    from features.meal.models.product import Product


class Store(UUIDAuditBase):
    __tablename__ = 'stores'

    name: Mapped[str] = mapped_column(String(255), unique=True)
    products: Mapped[List["Product"]] = relationship(back_populates="store")


class StoreRepository(SQLAlchemyAsyncRepository[Store]):
    model_type = Store


class StoreService(SQLAlchemyAsyncRepositoryService[Store]):
    repository_type = StoreRepository
