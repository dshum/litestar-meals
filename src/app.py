from advanced_alchemy.exceptions import ConflictError
from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from litestar import Litestar
from litestar.config.app import ExperimentalFeatures
from litestar.config.cors import CORSConfig
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR

from api import site_router
from lib import settings, database, sentry
from lib.exceptions import default_exception_handler
from lib.users import litestar_users

cors_config = CORSConfig(
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_credentials=True,
)

app = Litestar(
    route_handlers=[site_router],
    cors_config=cors_config,
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
