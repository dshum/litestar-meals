from advanced_alchemy import IntegrityError
from litestar import Request, Response
from litestar.exceptions import HTTPException, ValidationException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_409_CONFLICT
from sentry_sdk import capture_exception

from config import settings


def internal_server_error_handler(request: Request, exc: Exception) -> Response:
    if not settings.app.DEBUG:
        capture_exception(exc)

    return Response(
        content={
            "type": str(exc.__class__),
            "detail": getattr(exc, "detail", "No details provided"),
            "status_code": HTTP_500_INTERNAL_SERVER_ERROR,
        },
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    )


def http_exception_handler(request: Request, exc: HTTPException) -> Response:
    match exc:
        case IntegrityError():
            status_code = HTTP_409_CONFLICT
        case _:
            status_code = getattr(exc, "status_code", HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(
        content={
            "type": str(exc.__class__),
            "detail": getattr(exc, "detail", "No details provided"),
            "status_code": status_code,
        },
        status_code=status_code,
    )


def validation_exception_handler(request: Request, exc: ValidationException) -> Response:
    return Response(
        content={
            "type": str(exc.__class__),
            "detail": exc.detail,
            "status_code": exc.status_code,
            "extra": exc.extra,
        },
        status_code=exc.status_code,
    )
