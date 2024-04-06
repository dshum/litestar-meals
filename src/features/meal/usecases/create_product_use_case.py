from uuid import UUID

from features.meal.models.product import Product
from features.meal.schemas.product import ProductCreateSchema
from features.meal.services.brand_service import BrandService
from features.meal.services.product_service import ProductService
from features.meal.services.store_service import StoreService
from features.user.models.user import User


class CreateProductUseCase:
    def __init__(
            self,
            product_service: ProductService,
            brand_service: BrandService,
            store_service: StoreService,
    ):
        self.product_service: ProductService = product_service
        self.brand_service: BrandService = brand_service
        self.store_service: StoreService = store_service

    async def __call__(self, data: ProductCreateSchema, user: User) -> Product:
        product = await self.product_service.get_one_or_none(name=data.name, user=user)
        if product:
            return product

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

        product = Product(
            name=data.name,
            weight=data.weight,
            calories=data.calories,
            user_id=user.id,
            store_id=store.id,
            brand_id=brand.id,
        )
        return await self.product_service.create(product)
