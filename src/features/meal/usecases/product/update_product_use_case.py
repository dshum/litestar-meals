from uuid import UUID

from sqlalchemy import select

from features.meal.models.brand import BrandService
from features.meal.models.product import Product, ProductService
from features.meal.models.store import StoreService
from features.meal.schemas.product import ProductCreateSchema
from features.user.models.user import User


class UpdateProductUseCase:
    def __init__(
            self,
            product_service: ProductService,
            brand_service: BrandService,
            store_service: StoreService,
    ):
        self.product_service: ProductService = product_service
        self.brand_service: BrandService = brand_service
        self.store_service: StoreService = store_service

    async def __call__(
            self,
            data: ProductCreateSchema,
            id: UUID,
            user: User,
    ) -> Product:
        statement = select(Product).where(Product.user_id == user.id)
        try:
            product = await self.product_service.get(id, statement=statement)

            store, created = await self.store_service.get_or_upsert(
                match_fields=["name"],
                upsert=False,
                name=data.store_name,
            )

            brand, created = await self.brand_service.get_or_upsert(
                match_fields=["name"],
                upsert=False,
                name=data.brand_name,
            )

            data = ProductCreateSchema.model_dump(data, include={"name", "weight", "calories"})
            data.brand = brand
            data.store = store

            return await self.product_service.update(data, id)
        except:
            raise
