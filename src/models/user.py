from typing import List, TYPE_CHECKING, Any
from uuid import UUID

import bcrypt
from advanced_alchemy import SQLAlchemyAsyncRepository, SQLAlchemyAsyncRepositoryService
from advanced_alchemy.base import UUIDAuditBase
from litestar import Request
from litestar_users.adapter.sqlalchemy.mixins import SQLAlchemyUserMixin
from litestar_users.adapter.sqlalchemy.protocols import SQLAUserT
from litestar_users.service import BaseUserService
from sqlalchemy import String, select
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import UserMeal, Meal


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


class UserService(BaseUserService[User, Any]):
    async def post_registration_hook(self, user: User, request: Request | None = None) -> None:
        print(f"User <{user.email}> has registered!")

    async def post_login_hook(self, user: User, request: Request | None = None) -> None:
        print(f"User <{user.email}> logged in")
