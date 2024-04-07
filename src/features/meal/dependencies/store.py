from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from features.meal.models.store import StoreService, Store
from features.meal.usecases.store.get_stores_use_case import GetStoresUseCase


async def provide_get_stores_use_case(store_service: StoreService) -> GetStoresUseCase:
    return GetStoresUseCase(store_service=store_service)


async def provide_store_service(db_session: AsyncSession) -> StoreService:
    statement = select(Store).order_by(Store.name)
    return StoreService(session=db_session, statement=statement)
