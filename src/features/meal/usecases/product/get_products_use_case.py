from advanced_alchemy.filters import LimitOffset, OrderBy
from litestar.pagination import OffsetPagination
from sqlalchemy import select

from features.meal.models.product import Product
from features.meal.services.product_service import ProductService
from features.user.models.user import User


class GetProductsUseCase:
    def __init__(self, product_service: ProductService, limit_offset: LimitOffset, order_by: OrderBy):
        self.product_service: ProductService = product_service
        self.limit_offset: LimitOffset = limit_offset
        self.order_by: OrderBy = order_by

    async def __call__(self, user: User) -> OffsetPagination[Product]:
        statement = select(Product).where(Product.user_id == user.id)
        items, total = await self.product_service.list_and_count(
            self.limit_offset, self.order_by,
            statement=statement,
        )
        return OffsetPagination[Product](
            items=items,
            total=total,
            limit=self.limit_offset.limit,
            offset=self.limit_offset.offset,
        )
