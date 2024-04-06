from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from litestar import Litestar
from litestar.config.app import ExperimentalFeatures
from litestar.exceptions import HTTPException
from litestar.repository import ConflictError
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR

from config import settings, sentry
from config.cors import cors_config
from config.users import litestar_users
from core.database import sqlalchemy
from core.errors.handlers import default_exception_handler

from server.routes import router

app = Litestar(
    route_handlers=[router],
    cors_config=cors_config,
    plugins=[SQLAlchemyPlugin(sqlalchemy.db_config), litestar_users],
    on_startup=[sentry.on_startup, sqlalchemy.on_startup],
    exception_handlers={
        HTTP_500_INTERNAL_SERVER_ERROR: default_exception_handler,
        HTTPException: default_exception_handler,
        ConflictError: default_exception_handler,
    },
    debug=settings.app.DEBUG,
    experimental_features=[ExperimentalFeatures.DTO_CODEGEN],
)
