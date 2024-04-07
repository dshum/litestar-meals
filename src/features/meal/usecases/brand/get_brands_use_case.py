from typing import Sequence

from features.meal.models.brand import BrandService, Brand


class GetBrandsUseCase:
    def __init__(self, brand_service: BrandService):
        self.brand_service: BrandService = brand_service

    async def __call__(self) -> Sequence[Brand]:
        return await self.brand_service.list()
