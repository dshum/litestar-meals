from features.meal.models.brand import BrandService
from features.meal.models.product import Product, ProductService
from features.meal.models.store import StoreService
from features.meal.schemas.product import ProductCreateSchema

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
        product = await self.product_service.get_one_or_none(name=data.name, user_id=user.id)
        if product:
            return product

        product = Product(
            name=data.name,
            weight=data.weight,
            calories=data.calories,
            user_id=user.id,
        )

        if data.brand_name:
            brand, created = await self.brand_service.get_or_upsert(
                match_fields=["name"],
                upsert=False,
                name=data.brand_name,
            )
            product.brand_id = brand.id

        if data.store_name:
            store, created = await self.store_service.get_or_upsert(
                match_fields=["name"],
                upsert=False,
                name=data.store_name,
            )
            product.store_id = store.id

        return await self.product_service.create(product)
