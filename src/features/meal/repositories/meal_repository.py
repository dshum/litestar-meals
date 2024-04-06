from advanced_alchemy import SQLAlchemyAsyncRepository

from features.meal.models.meal import Meal


class MealRepository(SQLAlchemyAsyncRepository[Meal]):
    model_type = Meal
