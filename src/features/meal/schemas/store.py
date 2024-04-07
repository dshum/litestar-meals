from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.dto import DTOConfig

from features.meal.models.store import Store


class StoreReadDTO(SQLAlchemyDTO[Store]):
    config = DTOConfig(
        include={"id", "name"},
    )
