from uuid import UUID

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from advanced_alchemy.filters import LimitOffset, OrderBy
from litestar import Controller, get, post, put, delete, Request
from litestar.di import Provide
from litestar.dto import DTOConfig, DTOData
from litestar.pagination import OffsetPagination
from litestar.params import Parameter

from api.dependencies import (
    provide_meal_service,
    provide_limit_offset_pagination,
    provide_order_by,
    provide_user_meal_service,
)
from models import UserMeal
from models.meal import MealService
from models.user_meal import UserMealService


class ReadDTO(SQLAlchemyDTO[UserMeal]):
    config = DTOConfig(include={
        "id", "weight", "created_at",
        "user.id", "user.email", "user.first_name", "user.last_name",
        "meal.id", "meal.name", "meal.weight",
        "meal.brand.name", "meal.store.name",
    }, max_nested_depth=2)


class CreateDTO(SQLAlchemyDTO[UserMeal]):
    config = DTOConfig(include={"meal_id", "weight"})


class PatchDTO(SQLAlchemyDTO[UserMeal]):
    config = DTOConfig(include={"meal_id", "weight"}, partial=True)


class UserMealController(Controller):
    path = "/user/meals"
    dependencies = {
        "limit_offset": Provide(provide_limit_offset_pagination),
        "order_by": Provide(provide_order_by),
        "meal_service": Provide(provide_meal_service),
        "user_meal_service": Provide(provide_user_meal_service),
    }
    return_dto = ReadDTO

    @post(path="/", dto=CreateDTO)
    async def create_user_meal(
            self,
            request: Request,
            user_meal_service: UserMealService,
            meal_service: MealService,
            data: DTOData[UserMeal],
    ) -> UserMeal:
        data = data.create_instance(user_id=request.user.id)
        return await user_meal_service.create(data)

    @get(path="/")
    async def list_user_meals(
            self,
            user_meal_service: UserMealService,
            limit_offset: LimitOffset,
            order_by: OrderBy,
    ) -> OffsetPagination[UserMeal]:
        items, total = await user_meal_service.list_and_count(limit_offset, order_by)
        return OffsetPagination[UserMeal](
            items=items,
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )

    @get(path="/{user_meal_id:uuid}")
    async def get_user_meal(
            self,
            user_meal_service: UserMealService,
            user_meal_id: UUID = Parameter(
                title="User Meal ID",
                description="The user meal to retrieve",
            )
    ) -> UserMeal:
        return await user_meal_service.get(user_meal_id)

    @put(path="/{user_meal_id:uuid}", dto=PatchDTO)
    async def update_user_meal(
            self,
            user_meal_service: UserMealService,
            data: DTOData[UserMeal],
            user_meal_id: UUID = Parameter(
                title="User Meal ID",
                description="The user meal to update",
            )
    ) -> UserMeal:
        return await user_meal_service.update(data.create_instance(), user_meal_id)

    @delete(path="/{user_meal_id:uuid}", return_dto=None)
    async def delete_user_meal(
            self,
            user_meal_service: UserMealService,
            user_meal_id: UUID = Parameter(
                title="User Meal ID",
                description="The user meal to delete",
            ),
    ) -> None:
        await user_meal_service.delete(user_meal_id)
