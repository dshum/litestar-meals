from litestar import Router

from api.meal import MealController
from api.user_meal import UserMealController

site_router = Router(path="/", route_handlers=[
    MealController,
    UserMealController,
])
