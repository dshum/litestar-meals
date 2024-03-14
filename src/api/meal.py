from uuid import UUID

from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from advanced_alchemy.filters import LimitOffset, OrderBy
from litestar import Controller, get, post, put, delete, Request
from litestar.di import Provide
from litestar.dto import DTOConfig, DTOData
from litestar.pagination import OffsetPagination
from litestar.params import Parameter

from api.dependencies import provide_meal_service, provide_limit_offset_pagination, provide_order_by, \
    provide_meal_store_service, provide_meal_brand_service
from models.meal import MealService, Meal
from models.meal_brand import MealBrandService
from models.meal_store import MealStoreService


class ReadDTO(SQLAlchemyDTO[Meal]):
    config = DTOConfig(
        include={
            "id", "name", "weight", "calories", "created_at",
            "store.id", "store.name",
            "brand.id", "brand.name",
        },
    )


class CreateDTO(SQLAlchemyDTO[Meal]):
    config = DTOConfig(
        include={
            "name", "weight", "calories",
            "store.name", "brand.name",
        },
    )


class PatchDTO(SQLAlchemyDTO[Meal]):
    config = DTOConfig(
        include={"name", "weight", "calories"},
        partial=True,
    )


class MealController(Controller):
    path = "/meals"
    dependencies = {
        "limit_offset": Provide(provide_limit_offset_pagination),
        "order_by": Provide(provide_order_by),
        "meal_service": Provide(provide_meal_service),
        "meal_store_service": Provide(provide_meal_store_service),
        "meal_brand_service": Provide(provide_meal_brand_service),
    }
    return_dto = ReadDTO

    @post(path="/", dto=CreateDTO)
    async def create_meal(
            self,
            request: Request,
            meal_store_service: MealStoreService,
            meal_brand_service: MealBrandService,
            meal_service: MealService,
            data: DTOData[Meal],
    ) -> Meal:
        data = data.create_instance(user_id=request.user.id)
        data.store, created = await meal_store_service.get_or_upsert(
            match_fields=["name"],
            name=data.store.name,
        )
        data.brand, created = await meal_brand_service.get_or_upsert(
            match_fields=["name"],
            name=data.brand.name,
        )
        return await meal_service.create(data)

    @get(path="/")
    async def list_meals(
            self,
            meal_service: MealService,
            limit_offset: LimitOffset,
            order_by: OrderBy,
    ) -> OffsetPagination[Meal]:
        items, total = await meal_service.list_and_count(limit_offset, order_by)
        return OffsetPagination[Meal](
            items=items,
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )

    @get(path="/{meal_id:uuid}")
    async def get_meal(
            self,
            meal_service: MealService,
            meal_id: UUID = Parameter(
                title="Meal ID",
                description="The meal to retrieve",
            )
    ) -> Meal:
        return await meal_service.get(meal_id)

    @put(path="/{meal_id:uuid}", dto=PatchDTO)
    async def update_meal(
            self,
            meal_service: MealService,
            data: DTOData[Meal],
            meal_id: UUID = Parameter(
                title="Meal ID",
                description="The meal to update",
            )
    ) -> Meal:
        return await meal_service.update(data.create_instance(), meal_id)

    @delete(path="/{meal_id:uuid}", return_dto=None)
    async def delete_user(
            self,
            meal_service: MealService,
            meal_id: UUID = Parameter(
                title="Meal ID",
                description="The meal to delete",
            ),
    ) -> None:
        await meal_service.delete(meal_id, auto_commit=True)
