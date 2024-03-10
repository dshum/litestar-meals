from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar import post, Controller, get, Request, put, Response
from litestar.contrib.pydantic import PydanticDTO
from litestar.di import Provide
from litestar.dto import DTOConfig, DTOData
from litestar.exceptions import ValidationException, NotAuthorizedException, ClientException, NotFoundException
from litestar.params import Parameter

from api.dependencies import provide_user_service
from lib.jwt import jwt_auth
from models.user import UserService, User
from schemas.user import LoginUserSchema, UpdatePasswordSchema


class ReadDTO(SQLAlchemyDTO[User]):
    config = DTOConfig(exclude={"password", "created_meals", "meals", "updated_at"})


class CreateDTO(SQLAlchemyDTO[User]):
    config = DTOConfig(exclude={"created_meals", "meals", "created_at", "updated_at"})


class PatchDTO(SQLAlchemyDTO[User]):
    config = DTOConfig(exclude={"password", "created_meals", "meals", "created_at", "updated_at"}, partial=True)


class LoginDTO(PydanticDTO[LoginUserSchema]):
    pass


class UpdatePasswordDTO(PydanticDTO[UpdatePasswordSchema]):
    pass


class UserController(Controller):
    dependencies = {
        "user_service": Provide(provide_user_service),
    }
    return_dto = ReadDTO

    @post(path="/create90210", dto=CreateDTO)
    async def create_user(
            self,
            user_service: UserService,
            data: DTOData[User],
    ) -> User:
        return await user_service.create(data.create_instance())

    @post("/login")
    async def login(
            self,
            user_service: UserService,
            data: LoginUserSchema,
    ) -> Response[User]:
        user = await user_service.get_one_or_none(email=data.email)
        if not user:
            raise NotAuthorizedException("Invalid credentials")
        if not user.verify_password(data.password.get_secret_value()):
            raise NotAuthorizedException("Invalid credentials")
        return jwt_auth.login(
            identifier=str(user.id),
            token_extras={"email": user.email},
            response_body=user,
        )

    @get("/user")
    async def get_user(self, request: Request) -> User:
        return request.user

    @put(path="/user", dto=PatchDTO)
    async def update_user(
            self,
            request: Request,
            user_service: UserService,
            data: DTOData[User],
    ) -> User:
        data = data.create_instance()
        is_email_unique = await user_service.check_unique_email(data.email, request.user.id)
        if not is_email_unique:
            raise ValidationException("Validation failed", extra=[{
                "message": "This email already exists",
                "key": "email"
            }])
        return await user_service.update(data, request.user.id)

    @put(path="/password", dto=UpdatePasswordDTO)
    async def update_password(
            self,
            request: Request,
            user_service: UserService,
            data: DTOData[UpdatePasswordSchema],
    ) -> User:
        data = data.create_instance()
        current_password = data.current_password.get_secret_value()
        password = data.password.get_secret_value()

        if not request.user.verify_password(current_password):
            raise ValidationException("Validation failed", extra=[{
                "message": "Invalid current password",
                "key": "current_password"
            }])
        if data.password != data.confirm_password:
            raise ValidationException("Validation failed", extra=[{
                "message": "Passwords should match",
                "key": "confirm_password"
            }])

        return await user_service.update(User(password=password), request.user.id)
