from typing import List, TYPE_CHECKING, Any

import bcrypt
from advanced_alchemy.base import UUIDAuditBase
from litestar import Request
from litestar_users.adapter.sqlalchemy.mixins import SQLAlchemyUserMixin
from litestar_users.password import PasswordManager
from litestar_users.service import BaseUserService
from sqlalchemy import String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import UserMeal, Meal

password_manager = PasswordManager()


class User(UUIDAuditBase, SQLAlchemyUserMixin):
    __tablename__ = 'users'

    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    created_meals: Mapped[List["Meal"]] = relationship(
        foreign_keys="Meal.user_id",
        back_populates="creator",
        lazy="noload",
    )
    meals: Mapped[List["UserMeal"]] = relationship(
        foreign_keys="UserMeal.user_id",
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


class UserService(BaseUserService[User, Any]):
    async def post_registration_hook(self, user: User, request: Request | None = None) -> None:
        request.app.emit(event_id="user_registered", user_id=user.id)

    async def post_login_hook(self, user: User, request: Request | None = None) -> None:
        request.app.emit(event_id="user_logged", user_id=user.id)
