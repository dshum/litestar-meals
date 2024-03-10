from typing import Literal

from litestar import Request
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset, OrderBy
from sqlalchemy.ext.asyncio import AsyncSession

from models.meal import MealService
from models.user import UserService
from models.user_meal import UserMealService


async def provide_limit_offset_pagination(
        offset: int = Parameter(query="offset", ge=0, default=0, required=False),
        limit: int = Parameter(query="limit", ge=1, default=10, required=False),
) -> LimitOffset:
    return LimitOffset(limit, offset)


async def provide_order_by(
        sort_by: str = Parameter(default="created_at", required=False),
        sort_order: Literal["asc", "desc"] = Parameter(default="desc", required=False),
) -> OrderBy:
    return OrderBy(field_name=sort_by, sort_order=sort_order)


async def provide_user_service(db_session: AsyncSession) -> UserService:
    return UserService(session=db_session)


async def provide_meal_service(db_session: AsyncSession) -> MealService:
    return MealService(session=db_session)


async def provide_user_meal_service(db_session: AsyncSession) -> UserMealService:
    return UserMealService(session=db_session)
