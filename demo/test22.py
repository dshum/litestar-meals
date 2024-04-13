from dataclasses import dataclass

from litestar import Litestar, Response, Request, post
from litestar.dto import DTOData, DTOConfig, DataclassDTO
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR


def app_exception_handler(request: Request, exc: Exception) -> Response:
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


@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if len(self.name) < 3:
            raise ValueError("Name may not be shorter than 3 characters")
        if self.age < 21:
            raise ValueError("Min age is 21")


class PersonCreateDTO(DataclassDTO[Person]):
    pass


class PersonReadDTO(DataclassDTO[Person]):
    config = DTOConfig(include={"name"})


@post(path="/", dto=PersonCreateDTO, return_dto=PersonReadDTO)
async def create(data: DTOData[Person]) -> Person:
    data = data.create_instance()
    return data


app = Litestar(
    route_handlers=[create],
    exception_handlers={
        HTTP_500_INTERNAL_SERVER_ERROR: app_exception_handler,
        HTTPException: app_exception_handler,
    },
    debug=True,
)
