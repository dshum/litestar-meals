from advanced_alchemy import SQLAlchemyAsyncRepositoryService

from features.meal.models.store import Store
from features.meal.repositories.store_repository import StoreRepository


class StoreService(SQLAlchemyAsyncRepositoryService[Store]):
    repository_type = StoreRepository
