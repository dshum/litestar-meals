from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from features.meal.models.store import StoreService, Store
from features.meal.usecases.store_use_case import StoreUseCase
from features.user.models.user import User


async def provide_store_use_case(
        db_session: AsyncSession,
        current_user: User,
) -> StoreUseCase:
    statement = (select(Store)
                 .where(Store.user_id == current_user.id)
                 .order_by(Store.name))
    store_service = StoreService(session=db_session, statement=statement)
    return StoreUseCase(store_service=store_service)
