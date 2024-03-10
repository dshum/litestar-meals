from typing import List, TYPE_CHECKING, Any
from uuid import UUID

import bcrypt
from advanced_alchemy import SQLAlchemyAsyncRepository, SQLAlchemyAsyncRepositoryService
from advanced_alchemy.base import UUIDAuditBase
from litestar import Request
from litestar_users.adapter.sqlalchemy.mixins import SQLAlchemyUserMixin
from litestar_users.service import BaseUserService
from sqlalchemy import String, select
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from models import UserMeal, Meal


class User(UUIDAuditBase, SQLAlchemyUserMixin):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    _password: Mapped[str] = mapped_column("password_hash", String(1024))
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

    @hybrid_property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, new_password: str):
        new_password_hash = bcrypt.hashpw(
            password=new_password.encode(),
            salt=bcrypt.gensalt(rounds=10),
        )
        self._password = new_password_hash.decode()

    @property
    def name(self) -> bool:
        return self.first_name + " " + self.last_name

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(
            password=password.encode(),
            hashed_password=self.password.encode(),
        )


class User2Repository(SQLAlchemyAsyncRepository[User]):
    model_type = User


class User2Service(SQLAlchemyAsyncRepositoryService[User]):
    repository_type = User2Repository

    async def check_unique_email(self, email: str, user_id: UUID | None = None) -> bool:
        statement = select(User).where(User.email == email)
        if user_id:
            statement = statement.where(User.id != user_id)
        user_count = await self.count(statement=statement)
        return user_count < 1


class UserService(BaseUserService[User, Any]):
    async def post_registration_hook(self, user: User, request: Request | None = None) -> None:
        print(f"User <{user.email}> has registered!")
