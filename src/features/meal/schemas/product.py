from decimal import Decimal
from typing import Optional

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.contrib.pydantic import PydanticDTO
from litestar.dto import DTOConfig

from core.schemas.base_model import AppBaseModel
from features.meal.models.product import Product


class ProductCreateSchema(AppBaseModel):
    name: str
    weight: int
    calories: Decimal
    brand_name: Optional[str]
    store_name: Optional[str]


class ProductReadDTO(SQLAlchemyDTO[Product]):
    config = DTOConfig(
        include={
            "id", "name", "weight", "calories", "created_at",
            "store.id", "store.name",
            "brand.id", "brand.name",
        },
    )


class ProductCreateDTO(PydanticDTO[ProductCreateSchema]):
    pass


class ProductPatchDTO(PydanticDTO[ProductCreateSchema]):
    config = DTOConfig(partial=True)
