from advanced_alchemy.filters import LimitOffset, OrderBy
from litestar.pagination import OffsetPagination
from sqlalchemy import select

from features.meal.models.meal import Meal, MealService
from features.user.models.user import User


class GetMealsUseCase:
    def __init__(self, meal_service: MealService, limit_offset: LimitOffset, order_by: OrderBy):
        self.meal_service: MealService = meal_service
        self.limit_offset: LimitOffset = limit_offset
        self.order_by: OrderBy = order_by

    async def __call__(self, user: User) -> OffsetPagination[Meal]:
        statement = select(Meal).where(Meal.user_id == user.id)
        items, total = await self.meal_service.list_and_count(
            self.limit_offset, self.order_by,
            statement=statement,
        )
        return OffsetPagination[Meal](
            items=items,
            total=total,
            limit=self.limit_offset.limit,
            offset=self.limit_offset.offset,
        )
