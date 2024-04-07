from typing import Sequence

from litestar import Controller, get
from litestar.di import Provide

from features.meal.dependencies.store import provide_store_service, provide_get_stores_use_case
from features.meal.models.store import Store
from features.meal.schemas.store import StoreReadDTO
from features.meal.usecases.store.get_stores_use_case import GetStoresUseCase


class StoreController(Controller):
    path = "/stores"
    dependencies = {
        "get_stores_use_case": Provide(provide_get_stores_use_case),
        "store_service": Provide(provide_store_service),
    }
    return_dto = StoreReadDTO

    @get(path="/")
    async def get_stores(
            self,
            get_stores_use_case: GetStoresUseCase,
    ) -> Sequence[Store]:
        return await get_stores_use_case()
