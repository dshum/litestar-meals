from sqlalchemy import select

from features.meal.models.meal import Meal
from features.meal.models.product import Product
from features.meal.schemas.meal import MealCreateSchema
from features.meal.services.meal_service import MealService
from features.meal.services.product_service import ProductService
from features.user.models.user import User


class CreateMealUseCase:
    def __init__(
            self,
            meal_service: MealService,
            product_service: ProductService,
    ):
        self.meal_service: MealService = meal_service
        self.product_service: ProductService = product_service

    async def __call__(self, data: MealCreateSchema, user: User) -> Meal:
        statement = select(Product).where(Product.user_id == user.id)
        try:
            product = await self.product_service.get(data.product_id, statement=statement)
        except:
            raise

        meal = await self.meal_service.get_one_or_none(product_id=product.id, user_id=user.id)
        if meal:
            return meal

        meal = Meal(
            weight=data.weight or product.weight,
            product_id=product.id,
            user_id=user.id,
        )

        return await self.meal_service.create(meal)
