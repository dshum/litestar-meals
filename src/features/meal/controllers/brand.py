from dataclasses import dataclass
from typing import Sequence, Annotated

from advanced_alchemy import IntegrityError
from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar import Controller, get, post
from litestar.datastructures import UploadFile
from litestar.di import Provide
from litestar.dto import DTOConfig, DTOData
from litestar.enums import RequestEncodingType
from litestar.exceptions import HTTPException
from litestar.params import Body
from sqlalchemy.ext.asyncio import AsyncSession

from features.meal.dependencies.brand import provide_brand_service, provide_get_brands_use_case
from features.meal.models.brand import Brand, BrandService
from features.meal.schemas.brand import BrandReadDTO
from features.meal.usecases.brand.get_brands_use_case import GetBrandsUseCase


class BrandDTO(SQLAlchemyDTO[Brand]):
    config = DTOConfig(
        include={"name"},
    )


class BrandController(Controller):
    path = "/brands"
    dependencies = {
        "get_brands_use_case": Provide(provide_get_brands_use_case),
        "brand_service": Provide(provide_brand_service),
    }
    return_dto = BrandReadDTO


    @post("/", dto=BrandDTO, return_dto=None)
    async def create_brand(self, data: DTOData[Brand], db_session: AsyncSession) -> Brand | str:
        brand_service = BrandService(session=db_session)
        try:
            return await brand_service.create(data.create_instance())
        except IntegrityError:
            print("IntegrityError has been raised")
            # await db_session.rollback()
            raise HTTPException("Brand should be unique")
            # return "Brand should be unique"

    @get(path="/")
    async def get_brands(
            self,
            get_brands_use_case: GetBrandsUseCase,
    ) -> Sequence[Brand]:
        return await get_brands_use_case()
