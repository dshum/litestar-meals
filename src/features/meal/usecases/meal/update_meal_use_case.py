from uuid import UUID

from sqlalchemy import select

from features.meal.models.meal import Meal, MealService
from features.meal.schemas.meal import MealCreateSchema
from features.user.models.user import User


class UpdateMealUseCase:
    def __init__(self, meal_service: MealService):
        self.meal_service: MealService = meal_service

    async def __call__(
            self,
            data: MealCreateSchema,
            id: UUID,
            user: User,
    ) -> Meal:
        statement = select(Meal).where(Meal.user_id == user.id)
        try:
            meal = await self.meal_service.get(id, statement=statement)
            meal.weight = data.weight
            meal.product_id = data.product_id
            return await self.meal_service.update(meal, id)
        except:
            raise
