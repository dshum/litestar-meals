from typing import Optional
from uuid import UUID

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.contrib.pydantic import PydanticDTO
from litestar.dto import DTOConfig

from core.schemas.base_model import AppBaseModel
from features.meal.models.meal import Meal


class MealCreateSchema(AppBaseModel):
    weight: Optional[int]
    product_id: UUID


class MealCreateDTO(PydanticDTO[MealCreateSchema]):
    pass


class MealPatchDTO(PydanticDTO[MealCreateSchema]):
    config = DTOConfig(partial=True)


class MealReadDTO(SQLAlchemyDTO[Meal]):
    config = DTOConfig(
        include={
            "id", "weight", "created_at",
            "product.name", "product.weight", "product.calories",
            "product.brand.0.name", "product.store.0.name",
        },
        max_nested_depth=2,
    )
