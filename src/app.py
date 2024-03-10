from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from litestar import Litestar, get
from litestar.config.app import ExperimentalFeatures
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR

from api import site_router
from lib import settings, database, sentry
from lib.exceptions import default_exception_handler
from lib.jwt import jwt_auth



app = Litestar(
    route_handlers=[site_router],
    plugins=[SQLAlchemyPlugin(database.db_config)],
    on_startup=[sentry.on_startup, database.on_startup],
    on_app_init=[jwt_auth.on_app_init],
    exception_handlers={
        HTTP_500_INTERNAL_SERVER_ERROR: default_exception_handler,
        HTTPException: default_exception_handler,
    },
    debug=settings.app.DEBUG,
    experimental_features=[ExperimentalFeatures.DTO_CODEGEN],
)
