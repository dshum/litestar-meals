from math import floor, ceil

from advanced_alchemy.filters import LimitOffset, OrderBy
from litestar import Controller, get, post
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.pagination import ClassicPagination

from features.meal.dependencies.brand import provide_brand_use_case
from features.meal.models.brand import Brand
from features.meal.schemas.brand import BrandCreateDTO, BrandReadDTO, BrandCreateSchema
from features.meal.usecases.brand_use_case import BrandUseCase
from features.user.models.user import User


class BrandController(Controller):
    path = "/brands"
    dependencies = {
        "brand_use_case": Provide(provide_brand_use_case),
    }
    dto = BrandCreateDTO
    return_dto = BrandReadDTO

    @post("/")
    async def create_brand(
            self,
            data: DTOData[BrandCreateSchema],
            brand_use_case: BrandUseCase,
            current_user: User,
    ) -> Brand:
        data = data.create_instance(user_id=current_user.id)
        return await brand_use_case.create_brand(data)

    @get(path="/")
    async def get_brands(
            self,
            brand_use_case: BrandUseCase,
            limit_offset: LimitOffset,
            order_by: OrderBy,
    ) -> ClassicPagination[Brand]:
        items, total = await brand_use_case.get_brands(
            limit_offset=limit_offset,
            order_by=order_by,
        )
        return ClassicPagination[Brand](
            items=items,
            page_size=limit_offset.limit,
            current_page=floor(limit_offset.offset / limit_offset.limit) + 1,
            total_pages=ceil(total / limit_offset.limit)
        )
