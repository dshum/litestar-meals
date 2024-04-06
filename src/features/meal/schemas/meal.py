from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.dto import DTOConfig

from features.meal.models.meal import Meal


class MealReadDTO(SQLAlchemyDTO[Meal]):
    config = DTOConfig(include={
        "id", "weight", "created_at",
        "user.id", "user.email", "user.first_name", "user.last_name",
        "product.id", "product.name", "product.weight",
        "product.brand.name", "product.store.name",
    }, max_nested_depth=2)


class MealCreateDTO(SQLAlchemyDTO[Meal]):
    config = DTOConfig(include={"product_name", "weight"})


class MealPatchDTO(SQLAlchemyDTO[Meal]):
    config = DTOConfig(include={"product_name", "weight"}, partial=True)
