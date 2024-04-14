from math import floor, ceil
from uuid import UUID

from advanced_alchemy.filters import LimitOffset, OrderBy
from litestar import Controller, get, post, put, delete
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.pagination import ClassicPagination
from litestar.params import Parameter

from features.meal.dependencies.product import provide_product_use_case
from features.meal.models.product import Product
from features.meal.schemas.product import (
    ProductReadDTO,
    ProductCreateSchema,
    ProductPatchDTO,
    ProductCreateDTO,
)
from features.meal.usecases.product_use_case import ProductUseCase
from features.user.models.user import User


class ProductController(Controller):
    path = "/products"
    dependencies = {
        "product_use_case": Provide(provide_product_use_case),
    }
    return_dto = ProductReadDTO

    @post(path="/", dto=ProductCreateDTO)
    async def create_product(
            self,
            product_use_case: ProductUseCase,
            current_user: User,
            data: DTOData[ProductCreateSchema],
    ) -> Product:
        data = data.create_instance(user_id=current_user.id)
        return await product_use_case.create_product(data)

    @get(path="/")
    async def get_products(
            self,
            product_use_case: ProductUseCase,
            limit_offset: LimitOffset,
            order_by: OrderBy,
    ) -> ClassicPagination[Product]:
        items, total = await product_use_case.get_products(
            limit_offset=limit_offset,
            order_by=order_by,
        )
        return ClassicPagination[Product](
            items=items,
            page_size=limit_offset.limit,
            current_page=floor(limit_offset.offset / limit_offset.limit) + 1,
            total_pages=ceil(total / limit_offset.limit)
        )

    @get(path="/{id:uuid}")
    async def get_product(
            self,
            product_use_case: ProductUseCase,
            id: UUID = Parameter(
                title="Product ID",
                description="The product to retrieve",
            )
    ) -> Product:
        return await product_use_case.get_product(id)

    @put(path="/{id:uuid}", dto=ProductPatchDTO)
    async def update_product(
            self,
            product_use_case: ProductUseCase,
            current_user: User,
            data: DTOData[ProductCreateSchema],
            id: UUID = Parameter(
                title="Product ID",
                description="The product to update",
            )
    ) -> Product:
        data = data.create_instance(user_id=current_user.id)
        return await product_use_case.update_product(data, id)

    @delete(path="/{id:uuid}", return_dto=None)
    async def delete_product(
            self,
            product_use_case: ProductUseCase,
            id: UUID = Parameter(
                title="Product ID",
                description="The product to delete",
            ),
    ) -> None:
        await product_use_case.delete_product(id)
