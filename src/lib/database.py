from advanced_alchemy import AsyncSessionConfig
from advanced_alchemy.config import EngineConfig
from advanced_alchemy.extensions.litestar.plugins.init.config.asyncio import autocommit_before_send_handler
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig
from sqlalchemy.ext.asyncio import async_sessionmaker

from lib import settings
from models import Base

db_config = SQLAlchemyAsyncConfig(
    connection_string=settings.db.URL,
    metadata=Base.metadata,
    session_config=AsyncSessionConfig(expire_on_commit=False),
    engine_config=EngineConfig(echo=settings.db.ECHO),
    before_send_handler=autocommit_before_send_handler,
)

async_sessionmaker = async_sessionmaker(expire_on_commit=False)


async def on_startup() -> None:
    async with db_config.get_engine().begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
