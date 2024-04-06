from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from litestar_users import LitestarUsersPlugin

from config.alchemy import alchemy_config
from config.users import litestar_users_config

sqlalchemy_plugin = SQLAlchemyPlugin(config=alchemy_config)

litestar_users_plugin = LitestarUsersPlugin(
    config=litestar_users_config
)
