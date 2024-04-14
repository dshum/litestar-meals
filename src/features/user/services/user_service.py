from typing import Any

from litestar import Request
from litestar_users.schema import AuthenticationSchema
from litestar_users.service import BaseUserService

from features.user.models.user import User


class UserService(BaseUserService[User, Any]):
    async def post_registration_hook(self, user: User, request: Request | None = None) -> None:
        # request.app.emit(event_id="user_registered", user_id=user.id)
        pass

    async def pre_login_hook(self, data: AuthenticationSchema, request: Request | None = None) -> bool:
        print(request.cookies.get('csrftoken'))
        print(request.headers.get('x-csrftoken'))
        return True

    async def post_login_hook(self, user: User, request: Request | None = None) -> None:
        # request.app.emit(event_id="user_logged", user_id=user.id)
        pass
