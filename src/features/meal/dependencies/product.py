from advanced_alchemy.filters import LimitOffset, OrderBy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from features.meal.models.brand import BrandService
from features.meal.models.product import Product
from features.meal.models.product import ProductService
from features.meal.models.store import StoreService
from features.meal.usecases.product.create_product_use_case import CreateProductUseCase
from features.meal.usecases.product.delete_product_use_case import DeleteProductUseCase
from features.meal.usecases.product.get_product_use_case import GetProductUseCase
from features.meal.usecases.product.get_products_use_case import GetProductsUseCase
from features.meal.usecases.product.update_product_use_case import UpdateProductUseCase


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
    return GetProductsUseCase(
        product_service=product_service,
        limit_offset=limit_offset,
        order_by=order_by,
    )


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


async def provide_product_service(db_session: AsyncSession) -> ProductService:
    statement = (
        select(Product)
        # .options(selectinload(Product.user))
        .options(selectinload(Product.store))
        .options(selectinload(Product.brand))
    )
    return ProductService(session=db_session, statement=statement)
