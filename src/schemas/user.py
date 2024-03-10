from dataclasses import dataclass

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig
from litestar.dto import DataclassDTO
from pydantic import BaseModel, EmailStr, SecretStr

from models import User


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: SecretStr


class UpdatePasswordSchema(BaseModel):
    current_password: SecretStr
    password: SecretStr
    confirm_password: SecretStr


@dataclass
class UserRegistrationSchema(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str


class UserRegistrationDTO(DataclassDTO[UserRegistrationSchema]):
    """User registration DTO."""


class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"password_hash"})


class UserUpdateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"password_hash"}, partial=True)
