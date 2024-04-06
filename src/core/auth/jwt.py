from dataclasses import dataclass
from datetime import timedelta

from litestar.security.jwt import JWTCookieAuth
from litestar_users.user_handlers import jwt_retrieve_user_handler

from config import settings
from features.user.models.user import User


@dataclass
class AppJWTAuth[User](JWTCookieAuth):
    default_token_expiration: timedelta = timedelta(minutes=settings.jwt.TTL)


auth = AppJWTAuth[User](
    retrieve_user_handler=jwt_retrieve_user_handler,
    token_secret=settings.jwt.SECRET,
)
