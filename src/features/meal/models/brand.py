from typing import List, TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

if TYPE_CHECKING:
    from features.meal.models.product import Product


class Brand(UUIDAuditBase):
    __tablename__ = 'brands'

    name: Mapped[str] = mapped_column(String(255), unique=True)
    products: Mapped[List["Product"]] = relationship(back_populates="brand")
