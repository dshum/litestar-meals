from dataclasses import dataclass

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig
from litestar.dto import DataclassDTO

from models import User


@dataclass
class UserRegistrationSchema:
    email: str
    password: str
    first_name: str
    last_name: str


class UserRegistrationDTO(DataclassDTO[UserRegistrationSchema]):
    """User registration DTO."""


class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(
        include={"id", "first_name", "last_name", "email", "created_at"},
    )


class UserUpdateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(
        include={"new_password", "first_name", "last_name"},
        partial=True,
    )
