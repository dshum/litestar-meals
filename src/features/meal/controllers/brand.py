from typing import Sequence, Any

from litestar import Controller, get, post
from litestar.di import Provide
from litestar.dto import DTOData

from features.meal.dependencies.brand import (
    provide_brand_service,
    provide_get_brands_use_case,
    provide_create_brand_use_case,
)
from features.meal.models.brand import Brand
from features.meal.schemas.brand import BrandReadDTO, BrandCreateSchema, BrandCreateDTO
from features.meal.usecases.brand.create_brand_use_case import CreateBrandUseCase
from features.meal.usecases.brand.get_brands_use_case import GetBrandsUseCase


class BrandController(Controller):
    path = "/brands"
    dependencies = {
        "create_brand_use_case": Provide(provide_create_brand_use_case),
        "get_brands_use_case": Provide(provide_get_brands_use_case),
        "brand_service": Provide(provide_brand_service),
    }
    dto = BrandCreateDTO
    return_dto = BrandReadDTO

    @post("/")
    async def create_brand(
            self,
            data: DTOData[BrandCreateSchema],
            create_brand_use_case: CreateBrandUseCase,
    ) -> Any:
        data = data.create_instance()
        return await create_brand_use_case(data)

    @get(path="/")
    async def get_brands(
            self,
            get_brands_use_case: GetBrandsUseCase,
    ) -> Sequence[Brand]:
        return await get_brands_use_case()
