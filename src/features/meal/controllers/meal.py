from uuid import UUID

from litestar import Controller, get, post, put, delete, Request
from litestar.di import Provide
from litestar.pagination import OffsetPagination
from litestar.params import Parameter

from core.utils.dependencies import provide_limit_offset_pagination, provide_order_by
from features.meal.dependencies.meal import (
    provide_get_meals_use_case,
    provide_create_meal_use_case,
    provide_get_meal_use_case,
    provide_update_meal_use_case,
    provide_delete_meal_use_case,
    provide_meal_service,
)
from features.meal.dependencies.product import provide_product_service
from features.meal.models.meal import Meal
from features.meal.schemas.meal import MealReadDTO, MealCreateSchema, MealPatchDTO
from features.meal.usecases.meal.create_meal_use_case import CreateMealUseCase
from features.meal.usecases.meal.delete_meal_use_case import DeleteMealUseCase
from features.meal.usecases.meal.get_meal_use_case import GetMealUseCase
from features.meal.usecases.meal.get_meals_use_case import GetMealsUseCase
from features.meal.usecases.meal.update_meal_use_case import UpdateMealUseCase


class MealController(Controller):
    path = "/meals"
    dependencies = {
        "create_meal_use_case": Provide(provide_create_meal_use_case),
        "get_meals_use_case": Provide(provide_get_meals_use_case),
        "get_meal_use_case": Provide(provide_get_meal_use_case),
        "update_meal_use_case": Provide(provide_update_meal_use_case),
        "delete_meal_use_case": Provide(provide_delete_meal_use_case),
        "meal_service": Provide(provide_meal_service),
        "product_service": Provide(provide_product_service),
        "limit_offset": Provide(provide_limit_offset_pagination),
        "order_by": Provide(provide_order_by),
    }
    return_dto = MealReadDTO

    @post(path="/")
    async def create_meal(
            self,
            request: Request,
            create_meal_use_case: CreateMealUseCase,
            data: MealCreateSchema,
    ) -> Meal:
        return await create_meal_use_case(data, user=request.user)

    @get(path="/")
    async def get_meals(
            self,
            request: Request,
            get_meals_use_case: GetMealsUseCase,
    ) -> OffsetPagination[Meal]:
        return await get_meals_use_case(user=request.user)

    @get(path="/{id:uuid}")
    async def get_meal(
            self,
            request: Request,
            get_meal_use_case: GetMealUseCase,
            id: UUID = Parameter(
                title="Meal ID",
                description="The meal to retrieve",
            )
    ) -> Meal:
        return await get_meal_use_case(id, user=request.user)

    @put(path="/{id:uuid}", dto=MealPatchDTO)
    async def update_meal(
            self,
            request: Request,
            update_meal_use_case: UpdateMealUseCase,
            data: MealCreateSchema,
            id: UUID = Parameter(
                title="Meal ID",
                description="The meal to update",
            )
    ) -> Meal:
        return await update_meal_use_case(data, id, user=request.user)

    @delete(path="/{id:uuid}", return_dto=None)
    async def delete_meal(
            self,
            request: Request,
            delete_meal_use_case: DeleteMealUseCase,
            id: UUID = Parameter(
                title="Meal ID",
                description="The meal to delete",
            ),
    ) -> None:
        await delete_meal_use_case(id, user=request.user)
