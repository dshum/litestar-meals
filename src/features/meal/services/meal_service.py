from advanced_alchemy import SQLAlchemyAsyncRepositoryService

from features.meal.models.meal import Meal
from features.meal.repositories.meal_repository import MealRepository


class MealService(SQLAlchemyAsyncRepositoryService[Meal]):
    repository_type = MealRepository
