from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from features.meal.models.brand import BrandService, Brand
from features.meal.usecases.brand_use_case import BrandUseCase
from features.user.models.user import User


async def provide_brand_use_case(
        db_session: AsyncSession,
        current_user: User,
) -> BrandUseCase:
    statement = (select(Brand)
                 .where(Brand.user_id == current_user.id)
                 .order_by(Brand.name))
    brand_service = BrandService(session=db_session, statement=statement)
    return BrandUseCase(brand_service=brand_service)
