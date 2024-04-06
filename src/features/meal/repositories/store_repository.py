from advanced_alchemy import SQLAlchemyAsyncRepository

from features.meal.models.store import Store


class StoreRepository(SQLAlchemyAsyncRepository[Store]):
    model_type = Store
