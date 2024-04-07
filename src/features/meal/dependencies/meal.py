from advanced_alchemy.filters import LimitOffset, OrderBy
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from features.meal.models.meal import Meal
from features.meal.models.meal import MealService
from features.meal.models.product import Product
from features.meal.models.product import ProductService
from features.meal.usecases.meal.create_meal_use_case import CreateMealUseCase
from features.meal.usecases.meal.delete_meal_use_case import DeleteMealUseCase
from features.meal.usecases.meal.get_meal_use_case import GetMealUseCase
from features.meal.usecases.meal.get_meals_use_case import GetMealsUseCase
from features.meal.usecases.meal.update_meal_use_case import UpdateMealUseCase


async def provide_create_meal_use_case(
        meal_service: MealService,
        product_service: ProductService,
) -> CreateMealUseCase:
    return CreateMealUseCase(
        meal_service=meal_service,
        product_service=product_service,
    )


async def provide_get_meals_use_case(
        meal_service: MealService,
        limit_offset: LimitOffset,
        order_by: OrderBy,
) -> GetMealsUseCase:
    return GetMealsUseCase(
        meal_service=meal_service,
        limit_offset=limit_offset,
        order_by=order_by,
    )


async def provide_get_meal_use_case(meal_service: MealService) -> GetMealUseCase:
    return GetMealUseCase(meal_service=meal_service)


async def provide_update_meal_use_case(meal_service: MealService) -> UpdateMealUseCase:
    return UpdateMealUseCase(meal_service=meal_service)


async def provide_delete_meal_use_case(meal_service: MealService) -> DeleteMealUseCase:
    return DeleteMealUseCase(meal_service=meal_service)


async def provide_meal_service(db_session: AsyncSession) -> MealService:
    statement = (
        select(Meal)
        .options(selectinload(Meal.product).selectinload(Product.brand))
        .options(selectinload(Meal.product).selectinload(Product.store))
    )
    return MealService(session=db_session, statement=statement)
