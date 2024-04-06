from advanced_alchemy import SQLAlchemyAsyncRepository

from features.meal.models.product import Product


class ProductRepository(SQLAlchemyAsyncRepository[Product]):
    model_type = Product
