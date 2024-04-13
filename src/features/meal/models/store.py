from typing import List, TYPE_CHECKING
from uuid import UUID

from advanced_alchemy import SQLAlchemyAsyncRepository, SQLAlchemyAsyncRepositoryService
from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

if TYPE_CHECKING:
    from features.meal.models.product import Product
    from features.user.models.user import User


class Store(UUIDAuditBase):
    __tablename__ = 'stores'
    __table_args__ = (UniqueConstraint("name", "user_id"),)

    name: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True)
    user: Mapped["User"] = relationship(
        back_populates="stores",
        lazy="noload",
    )
    products: Mapped[List["Product"]] = relationship(back_populates="store")


class StoreRepository(SQLAlchemyAsyncRepository[Store]):
    model_type = Store


class StoreService(SQLAlchemyAsyncRepositoryService[Store]):
    repository_type = StoreRepository
