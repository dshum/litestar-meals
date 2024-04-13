from typing import Literal, Any

from advanced_alchemy.filters import LimitOffset, OrderBy
from litestar import Request
from litestar.params import Parameter
from litestar.security.jwt import Token

from features.user.models.user import User


async def provide_current_user(request: Request[User, Token, Any]) -> User:
    return request.user


async def provide_limit_offset_pagination(
        offset: int = Parameter(query="offset", ge=0, default=0, required=False),
        limit: int = Parameter(query="limit", ge=1, default=10, required=False),
) -> LimitOffset:
    return LimitOffset(limit, offset)


async def provide_classic_pagination(
        page: int = Parameter(query="page", ge=1, default=1, required=False),
        page_size: int = Parameter(query="pageSize", ge=1, le=100, default=10, required=False),
) -> LimitOffset:
    return LimitOffset(page_size, page_size * (page - 1))


async def provide_order_by(
        sort_by: str = Parameter(default="created_at", required=False),
        sort_order: Literal["asc", "desc"] = Parameter(default="desc", required=False),
) -> OrderBy:
    return OrderBy(field_name=sort_by, sort_order=sort_order)
