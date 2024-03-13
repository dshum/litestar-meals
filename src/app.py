from advanced_alchemy.exceptions import ConflictError
from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from litestar import Litestar
from litestar.config.app import ExperimentalFeatures
from litestar.exceptions import HTTPException
from litestar.security.jwt import JWTAuth
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from litestar_users import LitestarUsersConfig, LitestarUsersPlugin
from litestar_users.config import AuthHandlerConfig, RegisterHandlerConfig, VerificationHandlerConfig, \
    CurrentUserHandlerConfig, PasswordResetHandlerConfig

from api import site_router
from lib import settings, database, sentry
from lib.exceptions import default_exception_handler
from lib.jwt import CustomJWTAuth
from models.user import UserService, User
from schemas.user import UserRegistrationDTO, UserUpdateDTO, UserReadDTO

litestar_users = LitestarUsersPlugin(
    config=LitestarUsersConfig(
        auth_backend_class=CustomJWTAuth,
        secret=settings.jwt.SECRET,
        user_model=User,  # pyright: ignore
        user_read_dto=UserReadDTO,
        user_registration_dto=UserRegistrationDTO,
        user_update_dto=UserUpdateDTO,
        user_service_class=UserService,  # pyright: ignore
        auth_handler_config=AuthHandlerConfig(),
        register_handler_config=RegisterHandlerConfig(),
        verification_handler_config=VerificationHandlerConfig(),
        current_user_handler_config=CurrentUserHandlerConfig(),
        password_reset_handler_config=PasswordResetHandlerConfig(),
        auth_exclude_paths=['/schema', '/register', '/login'],
    )
)

app = Litestar(
    route_handlers=[site_router],
    plugins=[SQLAlchemyPlugin(database.db_config), litestar_users],
    on_startup=[sentry.on_startup, database.on_startup],
    exception_handlers={
        HTTP_500_INTERNAL_SERVER_ERROR: default_exception_handler,
        HTTPException: default_exception_handler,
        ConflictError: default_exception_handler,
    },
    debug=settings.app.DEBUG,
    experimental_features=[ExperimentalFeatures.DTO_CODEGEN],
)
