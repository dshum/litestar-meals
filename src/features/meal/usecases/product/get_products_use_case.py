from math import ceil, floor

from advanced_alchemy.filters import LimitOffset, OrderBy
from litestar.pagination import OffsetPagination, ClassicPagination
from sqlalchemy import select

from features.meal.models.product import Product, ProductService
from features.user.models.user import User


class GetProductsUseCase:
    def __init__(self, product_service: ProductService, limit_offset: LimitOffset, order_by: OrderBy):
        self.product_service: ProductService = product_service
        self.limit_offset: LimitOffset = limit_offset
        self.order_by: OrderBy = order_by

    async def __call__(self, user: User) -> ClassicPagination[Product]:
        statement = select(Product).where(Product.user_id == user.id)
        items, total = await self.product_service.list_and_count(
            self.limit_offset, self.order_by,
            statement=statement,
        )
        return ClassicPagination[Product](
            items=items,
            page_size=self.limit_offset.limit,
            current_page=floor(self.limit_offset.offset / self.limit_offset.limit) + 1,
            total_pages=ceil(total / self.limit_offset.limit)
        )
