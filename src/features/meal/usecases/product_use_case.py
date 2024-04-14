from dataclasses import asdict
from uuid import UUID

from advanced_alchemy import IntegrityError
from advanced_alchemy.filters import LimitOffset, OrderBy

from features.meal.models.product import ProductService, Product
from features.meal.schemas.product import ProductCreateSchema


class ProductUseCase:
    def __init__(self, product_service: ProductService):
        self.product_service = product_service

    async def create_product(self, data: ProductCreateSchema) -> Product:
        product_exists = await self.product_service.exists(name=data.name, user_id=data.user_id)
        if product_exists:
            raise IntegrityError("Product already exists")
        return await self.product_service.create(asdict(data))

    async def get_products(self, limit_offset: LimitOffset, order_by: OrderBy):
        return await self.product_service.list_and_count(limit_offset, order_by)

    async def get_product(self, id: UUID):
        return await self.product_service.get(id)

    async def update_product(self, data: ProductCreateSchema, id: UUID):
        return await self.product_service.update(asdict(data), id)

    async def delete_product(self, id: UUID):
        return await self.product_service.delete(id)
