from litestar import Router

from features.meal.controllers.brand import BrandController
from features.meal.controllers.store import StoreController
from features.user.controllers.user import UserController

router: Router = Router(path="/", route_handlers=[
    UserController,
    # ProductController,
    # MealController,
    BrandController,
    StoreController,
])
