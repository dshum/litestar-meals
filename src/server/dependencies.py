from litestar.di import Provide

from core.dependencies.dependencies import (
    provide_classic_pagination,
    provide_current_user,
    provide_order_by,
)

app_dependencies = {
    "current_user": Provide(provide_current_user),
    "limit_offset": Provide(provide_classic_pagination),
    "order_by": Provide(provide_order_by),
}
