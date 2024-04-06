from advanced_alchemy import SQLAlchemyAsyncRepositoryService

from features.meal.models.brand import Brand
from features.meal.repositories.brand_repository import BrandRepository


class BrandService(SQLAlchemyAsyncRepositoryService[Brand]):
    repository_type = BrandRepository
