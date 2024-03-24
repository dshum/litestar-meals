from typing import cast

from litestar import Controller, post, Response, Request
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.exceptions import NotAuthorizedException
from litestar_users.dependencies import provide_user_service
from litestar_users.schema import AuthenticationSchema

from lib.jwt import auth
from models import User
from models.user import UserService
from schemas.user import UserRegistrationDTO, UserReadDTO, UserRegistrationSchema


class UserController(Controller):
    """
    @post(
        path="/register/login",
        dependencies={"service": Provide(provide_user_service, sync_to_thread=False)},
        dto=UserRegistrationDTO,
        return_dto=UserReadDTO,
        exclude_from_auth=True,
    )
    async def register_and_login(
            self,
            request: Request,
            data: DTOData[UserRegistrationSchema],
            service: UserService,
    ) -> Response[User]:
        user = cast(User, await service.register(data.as_builtins(), request))
        return auth.login(identifier=str(user.id), response_body=cast(User, user))

    @post(
        "/login/unverified",
        dependencies={"service": Provide(provide_user_service, sync_to_thread=False)},
        return_dto=UserReadDTO,
        exclude_from_auth=True,
    )
    async def login_unverified(
            self,
            request: Request,
            data: AuthenticationSchema,
            service: UserService,
    ) -> Response[User]:
        user = await service.authenticate(data, request)
        if user is None:
            raise NotAuthorizedException(detail="login failed, invalid input")
        return auth.login(identifier=str(user.id), response_body=cast(User, user))
    """

    @post("/logout")
    async def logout(self, request: Request) -> None:
        request.cookies.pop(auth.key, None)
        request.clear_session()
