from dataclasses import asdict

from advanced_alchemy import IntegrityError
from advanced_alchemy.filters import LimitOffset, OrderBy

from features.meal.models.brand import BrandService, Brand
from features.meal.schemas.brand import BrandCreateSchema


class BrandUseCase:
    def __init__(self, brand_service: BrandService):
        self.brand_service = brand_service

    async def create_brand(self, data: BrandCreateSchema) -> Brand:
        brand_exists = await self.brand_service.exists(name=data.name, user_id=data.user_id)
        if brand_exists:
            raise IntegrityError("Brand already exists")
        return await self.brand_service.create(asdict(data))

    async def get_brands(self, limit_offset: LimitOffset, order_by: OrderBy):
        return await self.brand_service.list_and_count(limit_offset, order_by)
