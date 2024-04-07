from uuid import UUID

from sqlalchemy import select

from features.meal.models.meal import Meal, MealService
from features.user.models.user import User


class DeleteMealUseCase:
    def __init__(self, meal_service: MealService):
        self.meal_service: MealService = meal_service

    async def __call__(self, id: UUID, user: User) -> Meal:
        statement = select(Meal).where(Meal.user_id == user.id)
        try:
            meal = await self.meal_service.get(id, statement=statement)
            return await self.meal_service.delete(id)
        except:
            raise
