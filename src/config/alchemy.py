from advanced_alchemy import AsyncSessionConfig
from advanced_alchemy.config import EngineConfig
from advanced_alchemy.extensions.litestar.plugins.init.config.asyncio import autocommit_before_send_handler
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig

from config import settings
from core.models.base import Base

alchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.db.URL,
    metadata=Base.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=settings.db.ECHO),
    before_send_handler=autocommit_before_send_handler,
)
