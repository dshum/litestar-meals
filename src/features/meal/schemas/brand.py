from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.contrib.pydantic import PydanticDTO
from litestar.dto import DTOConfig
from pydantic import Field, EmailStr

from core.schemas.base_model import AppBaseModel
from features.meal.models.brand import Brand


class BrandCreateSchema(AppBaseModel):
    name: EmailStr
    age: int = Field(gt=21)


class BrandCreateDTO(PydanticDTO[BrandCreateSchema]):
    pass


class BrandReadDTO(SQLAlchemyDTO[Brand]):
    config = DTOConfig(
        include={"id", "name"},
    )
