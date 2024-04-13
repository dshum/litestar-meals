from sqlalchemy import select

from features.meal.models.brand import BrandService, Brand
from features.meal.schemas.brand import BrandCreateSchema


class CreateBrandUseCase:
    def __init__(self, brand_service: BrandService):
        self.brand_service = brand_service

    async def __call__(self, data: BrandCreateSchema) -> Brand:
        brand = await self.brand_service.get_one_or_none(name=data.name)
        if brand:
            return brand
        return await self.brand_service.create(data.dict())
