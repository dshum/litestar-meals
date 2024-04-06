from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig
from litestar.contrib.pydantic import PydanticDTO
from pydantic import BaseModel, Field

from features.user.models.user import User


class UserRegistrationSchema(BaseModel):
    email: str
    password: str = Field(min_length=6)
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)


class UserLoginSchema(BaseModel):
    email: str
    password: str


class UserRegistrationDTO(PydanticDTO[UserRegistrationSchema]):
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
