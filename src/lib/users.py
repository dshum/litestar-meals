from litestar_users import LitestarUsersPlugin
from litestar_users.config import (
    LitestarUsersConfig,
    AuthHandlerConfig,
    RegisterHandlerConfig,
    VerificationHandlerConfig,
    CurrentUserHandlerConfig,
    PasswordResetHandlerConfig,
)

from lib import settings
from lib.jwt import CustomJWTAuth
from models.user import UserService, User
from schemas.user import UserReadDTO, UserRegistrationDTO, UserUpdateDTO

litestar_users = LitestarUsersPlugin(
    config=LitestarUsersConfig(
        auth_backend_class=CustomJWTAuth,
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
        auth_exclude_paths=["/schema", "/register", "/login"],
    )
)
