from litestar_users.config import (
    LitestarUsersConfig,
    AuthHandlerConfig,
    RegisterHandlerConfig,
    VerificationHandlerConfig,
    CurrentUserHandlerConfig,
    PasswordResetHandlerConfig,
)

from config import settings
from features.user.guards.auth import AppJWTAuth
from features.user.models.user import User
from features.user.schemas.user import UserRegistrationDTO, UserUpdateDTO, UserReadDTO
from features.user.services.user_service import UserService

litestar_users_config = LitestarUsersConfig(
    auth_backend_class=AppJWTAuth,
    secret=settings.jwt.SECRET,
    user_model=User,  # pyright: ignore
    user_read_dto=UserReadDTO,
    user_registration_dto=UserRegistrationDTO,
    user_update_dto=UserUpdateDTO,
    user_service_class=UserService,
    auth_handler_config=AuthHandlerConfig(),
    register_handler_config=RegisterHandlerConfig(),
    verification_handler_config=VerificationHandlerConfig(),
    current_user_handler_config=CurrentUserHandlerConfig(),
    password_reset_handler_config=PasswordResetHandlerConfig(),
    auth_exclude_paths=["/schema", "/register", "/login", "/csrf-cookie"],
)
