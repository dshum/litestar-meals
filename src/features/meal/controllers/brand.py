from typing import Sequence

from litestar import Controller, get
from litestar.di import Provide

from features.meal.dependencies.brand import provide_brand_service, provide_get_brands_use_case
from features.meal.models.brand import Brand
from features.meal.schemas.brand import BrandReadDTO
from features.meal.usecases.brand.get_brands_use_case import GetBrandsUseCase


class BrandController(Controller):
    path = "/brands"
    dependencies = {
        "get_brands_use_case": Provide(provide_get_brands_use_case),
        "brand_service": Provide(provide_brand_service),
    }
    return_dto = BrandReadDTO

    @get(path="/")
    async def get_brands(
            self,
            get_brands_use_case: GetBrandsUseCase,
    ) -> Sequence[Brand]:
        return await get_brands_use_case()
