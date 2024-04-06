from typing import Literal

from advanced_alchemy.filters import LimitOffset, OrderBy
from litestar import Request
from litestar.params import Parameter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from features.meal.models.meal import Meal
from features.meal.models.product import Product
from features.meal.services.brand_service import BrandService
from features.meal.services.meal_service import MealService
from features.meal.services.product_service import ProductService
from features.meal.services.store_service import StoreService
from features.meal.usecases.create_product_use_case import CreateProductUseCase
from features.meal.usecases.delete_product_use_case import DeleteProductUseCase
from features.meal.usecases.get_product_use_case import GetProductUseCase
from features.meal.usecases.get_products_use_case import GetProductsUseCase
from features.meal.usecases.update_product_use_case import UpdateProductUseCase


async def provide_create_product_use_case(
        product_service: ProductService,
        brand_service: BrandService,
        store_service: StoreService,
) -> CreateProductUseCase:
    return CreateProductUseCase(
        product_service=product_service,
        brand_service=brand_service,
        store_service=store_service,
    )


async def provide_get_products_use_case(
        product_service: ProductService,
        limit_offset: LimitOffset,
        order_by: OrderBy,
) -> GetProductsUseCase:
    return GetProductsUseCase(product_service=product_service, limit_offset=limit_offset, order_by=order_by)


async def provide_get_product_use_case(product_service: ProductService) -> GetProductUseCase:
    return GetProductUseCase(product_service=product_service)


async def provide_update_product_use_case(
        product_service: ProductService,
        brand_service: BrandService,
        store_service: StoreService,
) -> UpdateProductUseCase:
    return UpdateProductUseCase(
        product_service=product_service,
        brand_service=brand_service,
        store_service=store_service,
    )


async def provide_delete_product_use_case(product_service: ProductService) -> DeleteProductUseCase:
    return DeleteProductUseCase(product_service=product_service)


async def provide_store_service(db_session: AsyncSession) -> StoreService:
    return StoreService(session=db_session)


async def provide_brand_service(db_session: AsyncSession) -> BrandService:
    return BrandService(session=db_session)


async def provide_product_service(db_session: AsyncSession) -> ProductService:
    statement = (
        select(Product)
        .options(selectinload(Product.store))
        .options(selectinload(Product.brand))
    )
    return ProductService(session=db_session, statement=statement)


async def provide_meal_service(db_session: AsyncSession) -> MealService:
    statement = (
        select(Meal)
        .options(selectinload(Meal.product).selectinload(Product.brand))
        .options(selectinload(Meal.product).selectinload(Product.store))
    )
    return MealService(session=db_session, statement=statement)
