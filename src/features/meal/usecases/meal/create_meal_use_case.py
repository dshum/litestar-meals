from sqlalchemy import select

from features.meal.models.meal import Meal, MealService
from features.meal.models.product import Product, ProductService
from features.meal.schemas.meal import MealCreateSchema
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
        product = await self.product_service.get(data.product_id, statement=statement)

        meal = Meal(
            weight=data.weight or product.weight,
            product_id=product.id,
            user_id=user.id,
        )

        return await self.meal_service.create(meal)
