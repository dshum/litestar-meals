from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from uuid import UUID

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.dto import DTOConfig, DataclassDTO

from features.meal.models.product import Product


@dataclass
class ProductCreateSchema:
    name: str
    weight: int
    calories: Decimal
    user_id: UUID
    brand_id: Optional[UUID] = None
    store_id: Optional[UUID] = None


class ProductCreateDTO(DataclassDTO[ProductCreateSchema]):
    config = DTOConfig(
        include={"name", "weight", "calories", "brand_id", "store_id"},
    )


class ProductPatchDTO(DataclassDTO[ProductCreateSchema]):
    config = DTOConfig(
        include={"name", "weight", "calories", "brand_id", "store_id"},
        partial=True,
    )


class ProductReadDTO(SQLAlchemyDTO[Product]):
    config = DTOConfig(
        include={
            "id", "name", "weight", "calories", "created_at",
            "brand.0.name", "store.0.name",
        },
    )
