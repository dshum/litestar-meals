from dataclasses import dataclass
from datetime import timedelta

from litestar.security.jwt import JWTCookieAuth
from litestar_users.user_handlers import jwt_retrieve_user_handler

from lib import settings
from models import User


@dataclass
class CustomJWTAuth[User](JWTCookieAuth):
    default_token_expiration: timedelta = timedelta(minutes=settings.jwt.TTL)


auth = CustomJWTAuth[User](
    retrieve_user_handler=jwt_retrieve_user_handler,
    token_secret=settings.jwt.SECRET,
)
