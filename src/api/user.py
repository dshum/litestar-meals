from typing import cast

from litestar import Controller, post, Response, Request
from litestar.di import Provide
from litestar.exceptions import NotAuthorizedException, PermissionDeniedException
from litestar_users.dependencies import provide_user_service

from lib.jwt import auth
from models import User
from models.user import UserService
from schemas.user import UserReadDTO, UserRegistrationSchema, UserLoginSchema


class UserController(Controller):
    """
    @post(
        path="/register",
        dependencies={"service": Provide(provide_user_service, sync_to_thread=False)},
        return_dto=UserReadDTO,
        exclude_from_auth=True,
    )
    async def register(
            self,
            request: Request,
            data: UserRegistrationSchema,
            service: UserService,
    ) -> User:
        data = data.dict()
        return cast(User, await service.register(data, request))

    @post(
        "/login",
        dependencies={"service": Provide(provide_user_service, sync_to_thread=False)},
        return_dto=UserReadDTO,
        exclude_from_auth=True,
    )
    async def login(
            self,
            request: Request,
            data: UserLoginSchema,
            service: UserService,
    ) -> Response[User]:
        user = await service.authenticate(data, request)
        if user is None:
            raise NotAuthorizedException(detail="Incorrect email or password")
        if user.is_verified is False:
            raise PermissionDeniedException(detail="User is not verified")
        return auth.login(identifier=str(user.id), response_body=cast(User, user))
    """

    @post("/logout")
    async def logout(self, request: Request) -> None:
        request.cookies.pop(auth.key, None)
        request.clear_session()
