from uuid import UUID

from sqlalchemy import select

from features.meal.models.product import Product, ProductService
from features.user.models.user import User


class GetProductUseCase:
    def __init__(self, product_service: ProductService):
        self.product_service: ProductService = product_service

    async def __call__(self, id: UUID, user: User) -> Product:
        statement = select(Product).where(Product.user_id == user.id)
        return await self.product_service.get(id, statement=statement)
