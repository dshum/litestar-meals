from advanced_alchemy import SQLAlchemyAsyncRepository

from features.meal.models.brand import Brand


class BrandRepository(SQLAlchemyAsyncRepository[Brand]):
    model_type = Brand
