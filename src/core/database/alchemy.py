from sqlalchemy.ext.asyncio import async_sessionmaker

from config.alchemy import alchemy_config
from core.models.base import Base

async_sessionmaker = async_sessionmaker(expire_on_commit=False)


async def on_startup() -> None:
    async with alchemy_config.get_engine().begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
