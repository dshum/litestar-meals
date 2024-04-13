from dataclasses import dataclass
from uuid import UUID

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.dto import DTOConfig, DataclassDTO

from features.meal.models.brand import Brand


@dataclass
class BrandCreateSchema:
    name: str
    user_id: UUID


class BrandCreateDTO(DataclassDTO[BrandCreateSchema]):
    config = DTOConfig(include={"name"})


class BrandReadDTO(SQLAlchemyDTO[Brand]):
    config = DTOConfig(include={"id", "name"})
