from advanced_alchemy import IntegrityError
from litestar import Litestar
from litestar.exceptions import HTTPException, ValidationException, SerializationException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from pydantic_core import ValidationError

from config import settings
from config.cors import cors_config
from core.database import alchemy
from core.errors import sentry
from core.errors.handlers import (
    default_exception_handler,
    validation_exception_handler,
)
from server.dependencies import app_dependencies
from server.plugins import litestar_users_plugin, sqlalchemy_plugin
from server.routes import router

app = Litestar(
    route_handlers=[router],
    cors_config=cors_config,
    dependencies=app_dependencies,
    plugins=[sqlalchemy_plugin, litestar_users_plugin],
    on_startup=[sentry.on_startup, alchemy.on_startup],
    exception_handlers={
        HTTP_500_INTERNAL_SERVER_ERROR: default_exception_handler,
        HTTPException: default_exception_handler,
        IntegrityError: default_exception_handler,
    },
    debug=settings.app.DEBUG,
)
