from dataclasses import dataclass
from uuid import UUID

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.dto import DTOConfig, DataclassDTO

from features.meal.models.store import Store


@dataclass
class StoreCreateSchema:
    name: str
    user_id: UUID


class StoreCreateDTO(DataclassDTO[StoreCreateSchema]):
    config = DTOConfig(include={"name"})


class StoreReadDTO(SQLAlchemyDTO[Store]):
    config = DTOConfig(include={"id", "name"})
