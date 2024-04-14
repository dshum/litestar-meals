from typing import Any

from litestar import Litestar, Response, Request, get
from litestar.exceptions import HTTPException, ClientException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from litestar.types import Message, Scope


def default_exception_handler(request: Request, exc: HTTPException) -> Response:
    print("default_exception_handler", exc)
    # traceback.print_exception(exc)

    status_code = getattr(exc, "status_code", "500")
    content = {
        "type": str(exc.__class__),
        "detail": getattr(exc, "detail", "Error without detail"),
        "status_code": status_code,
    }

    if hasattr(exc, "extra") and exc.extra:
        content.update({"extra": exc.extra})

    return Response(
        content=content,
        status_code=status_code,
    )


count = 0


async def before_send_hook_handler(message: Message, scope: Scope) -> None:
    global count
    print("Count = ", count)
    count += 1
    if count < 2:
        raise ClientException("Crash! Boom!")
    pass


@get(path="/")
async def index() -> dict[str, Any]:
    return {"status": "OK"}


app = Litestar(
    route_handlers=[index],
    before_send=[before_send_hook_handler],
    exception_handlers={
        HTTP_500_INTERNAL_SERVER_ERROR: default_exception_handler,
        HTTPException: default_exception_handler,
    },
    debug=False,
)
