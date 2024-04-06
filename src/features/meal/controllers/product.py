from uuid import UUID

from litestar import Controller, get, post, put, delete, Request
from litestar.di import Provide
from litestar.pagination import OffsetPagination
from litestar.params import Parameter

from core.dependencies import provide_limit_offset_pagination, provide_order_by
from features.meal.dependencies import (
    provide_get_products_use_case,
    provide_create_product_use_case,
    provide_get_product_use_case,
    provide_update_product_use_case,
    provide_delete_product_use_case,
    provide_product_service,
    provide_brand_service,
    provide_store_service,
)
from features.meal.models.product import Product
from features.meal.schemas.product import ProductReadDTO, ProductCreateSchema, ProductPatchDTO
from features.meal.usecases.create_product_use_case import CreateProductUseCase
from features.meal.usecases.delete_product_use_case import DeleteProductUseCase
from features.meal.usecases.get_product_use_case import GetProductUseCase
from features.meal.usecases.get_products_use_case import GetProductsUseCase
from features.meal.usecases.update_product_use_case import UpdateProductUseCase


class ProductController(Controller):
    path = "/products"
    dependencies = {
        "create_product_use_case": Provide(provide_create_product_use_case),
        "get_products_use_case": Provide(provide_get_products_use_case),
        "get_product_use_case": Provide(provide_get_product_use_case),
        "update_product_use_case": Provide(provide_update_product_use_case),
        "delete_product_use_case": Provide(provide_delete_product_use_case),
        "product_service": Provide(provide_product_service),
        "brand_service": Provide(provide_brand_service),
        "store_service": Provide(provide_store_service),
        "limit_offset": Provide(provide_limit_offset_pagination),
        "order_by": Provide(provide_order_by),
    }
    return_dto = ProductReadDTO

    @post(path="/", dto=None)
    async def create_product(
            self,
            request: Request,
            create_product_use_case: CreateProductUseCase,
            data: ProductCreateSchema,
    ) -> Product:
        return await create_product_use_case(data, user=request.user)

    @get(path="/")
    async def get_products(
            self,
            request: Request,
            get_products_use_case: GetProductsUseCase,
    ) -> OffsetPagination[Product]:
        return await get_products_use_case(user=request.user)

    @get(path="/{id:uuid}")
    async def get_product(
            self,
            request: Request,
            get_product_use_case: GetProductUseCase,
            id: UUID = Parameter(
                title="Product ID",
                description="The product to retrieve",
            )
    ) -> Product:
        return await get_product_use_case(id, user=request.user)

    @put(path="/{id:uuid}", dto=ProductPatchDTO)
    async def update_product(
            self,
            request: Request,
            update_product_use_case: UpdateProductUseCase,
            data: ProductCreateSchema,
            id: UUID = Parameter(
                title="Product ID",
                description="The product to update",
            )
    ) -> Product:
        return await update_product_use_case(data, id, user=request.user)

    @delete(path="/{id:uuid}", return_dto=None)
    async def delete_product(
            self,
            request: Request,
            delete_product_use_case: DeleteProductUseCase,
            id: UUID = Parameter(
                title="Product ID",
                description="The product to delete",
            ),
    ) -> None:
        await delete_product_use_case(id, user=request.user)
