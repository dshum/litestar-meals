from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from features.meal.models.brand import BrandService, Brand
from features.meal.usecases.brand.get_brands_use_case import GetBrandsUseCase


async def provide_get_brands_use_case(brand_service: BrandService) -> GetBrandsUseCase:
    return GetBrandsUseCase(brand_service=brand_service)


async def provide_brand_service(db_session: AsyncSession) -> BrandService:
    statement = select(Brand).order_by(Brand.name)
    return BrandService(session=db_session, statement=statement)
