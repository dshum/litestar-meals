from dataclasses import asdict
from uuid import UUID

from advanced_alchemy import IntegrityError
from advanced_alchemy.filters import LimitOffset, OrderBy

from features.meal.models.store import StoreService, Store
from features.meal.schemas.store import StoreCreateSchema


class StoreUseCase:
    def __init__(self, store_service: StoreService):
        self.store_service = store_service

    async def create_store(self, data: StoreCreateSchema) -> Store:
        store_exists = await self.store_service.exists(name=data.name, user_id=data.user_id)
        if store_exists:
            raise IntegrityError("Store already exists")
        return await self.store_service.create(asdict(data))

    async def get_stores(self, limit_offset: LimitOffset, order_by: OrderBy):
        return await self.store_service.list_and_count(limit_offset, order_by)

    async def get_store(self, id: UUID):
        return await self.store_service.get(id)

    async def update_store(self, data: StoreCreateSchema, id: UUID):
        return await self.store_service.update(asdict(data), id)

    async def delete_store(self, id: UUID):
        return await self.store_service.delete(id)
