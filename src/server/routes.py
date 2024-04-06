from litestar import Router

from features.meal.controllers.meal import MealController
from features.meal.controllers.product import ProductController
from features.user.controllers.user import UserController

router: Router = Router(path="/", route_handlers=[
    UserController,
    ProductController,
    MealController,
])
