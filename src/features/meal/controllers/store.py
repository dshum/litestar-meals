from math import floor, ceil
from typing import Any

from advanced_alchemy.filters import LimitOffset, OrderBy
from litestar import Controller, get, post
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.pagination import ClassicPagination

from features.meal.dependencies.store import provide_store_use_case
from features.meal.models.store import Store
from features.meal.schemas.store import StoreCreateDTO, StoreReadDTO, StoreCreateSchema
from features.meal.usecases.store_use_case import StoreUseCase
from features.user.models.user import User


class StoreController(Controller):
    path = "/stores"
    dependencies = {
        "store_use_case": Provide(provide_store_use_case),
    }
    dto = StoreCreateDTO
    return_dto = StoreReadDTO

    @post("/")
    async def create_store(
            self,
            data: DTOData[StoreCreateSchema],
            store_use_case: StoreUseCase,
            current_user: User,
    ) -> Store:
        data = data.create_instance(user_id=current_user.id)
        return await store_use_case.create_store(data)

    @get(path="/")
    async def get_stores(
            self,
            store_use_case: StoreUseCase,
            limit_offset: LimitOffset,
            order_by: OrderBy,
    ) -> ClassicPagination[Store]:
        items, total = await store_use_case.get_stores(
            limit_offset=limit_offset,
            order_by=order_by,
        )
        return ClassicPagination[Store](
            items=items,
            page_size=limit_offset.limit,
            current_page=floor(limit_offset.offset / limit_offset.limit) + 1,
            total_pages=ceil(total / limit_offset.limit)
        )
