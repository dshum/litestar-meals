from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.dto import DTOConfig

from features.meal.models.brand import Brand


class BrandReadDTO(SQLAlchemyDTO[Brand]):
    config = DTOConfig(
        include={"id", "name"},
    )
