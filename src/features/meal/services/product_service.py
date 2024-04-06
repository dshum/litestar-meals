from advanced_alchemy import SQLAlchemyAsyncRepositoryService

from features.meal.models.product import Product
from features.meal.repositories.product_repository import ProductRepository


class ProductService(SQLAlchemyAsyncRepositoryService[Product]):
    repository_type = ProductRepository
