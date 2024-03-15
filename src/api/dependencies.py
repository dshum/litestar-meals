from typing import Literal

from litestar import Request
from litestar.params import Parameter
from litestar.repository.filters import LimitOffset, OrderBy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models.meal import MealService, Meal
from models.meal_brand import MealBrandService
from models.meal_store import MealStoreService
from models.user_meal import UserMealService, UserMeal


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


async def provide_meal_store_service(db_session: AsyncSession) -> MealStoreService:
    return MealStoreService(session=db_session)


async def provide_meal_brand_service(db_session: AsyncSession) -> MealBrandService:
    return MealBrandService(session=db_session)


async def provide_meal_service(db_session: AsyncSession) -> MealService:
    return MealService(
        statement=select(Meal).options(selectinload(Meal.store), selectinload(Meal.brand)),
        session=db_session,
    )


async def provide_user_meal_service(request: Request, db_session: AsyncSession) -> UserMealService:
    statement = (
        select(UserMeal)
        .where(UserMeal.user_id == request.user.id)
        .options(selectinload(UserMeal.meal).selectinload(Meal.brand))
        .options(selectinload(UserMeal.meal).selectinload(Meal.store))
    )
    return UserMealService(
        statement=statement,
        session=db_session,
    )
