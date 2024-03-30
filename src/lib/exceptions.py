from litestar import Request, Response
from litestar.exceptions import HTTPException
from sentry_sdk import capture_exception


def default_exception_handler(request: Request, exc: HTTPException) -> Response:
    capture_exception(exc)

    if hasattr(exc, "detail"):
        detail = exc.detail
    elif exc:
        detail = exc
    else:
        detail = "Internal server error"
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
