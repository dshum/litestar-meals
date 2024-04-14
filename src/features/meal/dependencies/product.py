from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from features.meal.models.product import Product
from features.meal.models.product import ProductService
from features.meal.usecases.product_use_case import ProductUseCase
from features.user.models.user import User


async def provide_product_use_case(
        db_session: AsyncSession,
        current_user: User,
) -> ProductUseCase:
    statement = (select(Product)
                 .options(selectinload(Product.store))
                 .options(selectinload(Product.brand))
                 .where(Product.user_id == current_user.id)
                 .order_by(Product.name))
    product_service = ProductService(session=db_session, statement=statement)
    return ProductUseCase(product_service=product_service)
