from typing import List, TYPE_CHECKING

from advanced_alchemy.base import UUIDAuditBase
from litestar_users.adapter.sqlalchemy.mixins import SQLAlchemyUserMixin
from litestar_users.password import PasswordManager
from sqlalchemy import String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from features.meal.models.meal import Meal
from features.meal.models.product import Product

password_manager = PasswordManager()


class User(UUIDAuditBase, SQLAlchemyUserMixin):
    __tablename__ = 'users'

    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    products: Mapped[List[Product]] = relationship(
        foreign_keys="Product.user_id",
        back_populates="user",
        lazy="noload",
    )
    meals: Mapped[List["Meal"]] = relationship(
        foreign_keys="Meal.user_id",
        back_populates="user",
        lazy="noload",
    )

    @property
    def name(self) -> bool:
        return self.first_name + " " + self.last_name

    @hybrid_property
    def new_password(self) -> str:
        return self.password_hash

    @new_password.setter
    def new_password(self, new_password: str):
        self.password_hash = password_manager.hash(new_password)
