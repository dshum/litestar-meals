from typing import Sequence

from features.meal.models.store import StoreService, Store


class GetStoresUseCase:
    def __init__(self, store_service: StoreService):
        self.store_service: StoreService = store_service

    async def __call__(self) -> Sequence[Store]:
        return await self.store_service.list()
