from litestar import Litestar, Response, Request, post
from litestar.contrib.pydantic import PydanticDTO
from litestar.dto import DTOData, DTOConfig
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from pydantic import BaseModel, EmailStr, Field


def app_exception_handler(request: Request, exc: HTTPException) -> Response:
    detail = exc.detail if hasattr(exc, "detail") else "Something wrong"
    status_code = exc.status_code if hasattr(exc, "status_code") else 500
    content = {
        "type": str(exc.__class__),
        "detail": detail,
        "status_code": status_code,
    }

    if hasattr(exc, "extra") and exc.extra:
        content.update({"extra": exc.extra})

    return Response(
        content=content,
        status_code=status_code,
    )


class Person(BaseModel):
    email: EmailStr
    name: str = Field(min_length=3)
    age: int = Field(ge=21)


class PersonCreateDTO(PydanticDTO[Person]):
    pass


class PersonReadDTO(PydanticDTO[Person]):
    config = DTOConfig(include={"name", "age"})


@post(path="/", dto=PersonCreateDTO, return_dto=PersonReadDTO)
async def create(data: DTOData[Person]) -> Person:
    """
    Returns ValidationError without extra field
    {
        "type": "<class 'pydantic_core._pydantic_core.ValidationError'>",
        "detail": "Something wrong",
        "status_code": 500
    }
    """
    data = data.create_instance()
    return data


@post(path="/without_dto")
async def create_without_dto(data: Person) -> Person:
    """
    Returns ValidationException with all validation errors:
    {
        "type": "<class 'litestar.exceptions.http_exceptions.ValidationException'>",
        "detail": "Validation failed for POST /without_dto",
        "status_code": 400,
        "extra": [
            {
                "message": "value is not a valid email address: The email address is not valid. It must have exactly one @-sign.",
                "key": "email"
            },
            {
                "message": "String should have at least 3 characters",
                "key": "name"
            },
            {
                "message": "Input should be greater than or equal to 21",
                "key": "age"
            }
        ]
    }
    """
    return data


app = Litestar(
    route_handlers=[create, create_without_dto],
    exception_handlers={
        HTTP_500_INTERNAL_SERVER_ERROR: app_exception_handler,
        HTTPException: app_exception_handler,
    },
    debug=True,
)
