from dataclasses import asdict
from uuid import UUID

from advanced_alchemy import IntegrityError
from advanced_alchemy.filters import LimitOffset, OrderBy

from features.meal.models.brand import BrandService, Brand
from features.meal.schemas.brand import BrandCreateSchema


class BrandUseCase:
    def __init__(self, brand_service: BrandService):
        self.brand_service = brand_service

    async def create_brand(self, data: BrandCreateSchema) -> Brand:
        try:
            return await self.brand_service.create(asdict(data))
        except IntegrityError as e:
            e.detail = "Brand already exists"
            raise

    async def get_brands(self, limit_offset: LimitOffset, order_by: OrderBy):
        return await self.brand_service.list_and_count(limit_offset, order_by)

    async def get_brand(self, id: UUID):
        return await self.brand_service.get(id)

    async def update_brand(self, data: BrandCreateSchema, id: UUID):
        return await self.brand_service.update(asdict(data), id)

    async def delete_brand(self, id: UUID):
        return await self.brand_service.delete(id)
