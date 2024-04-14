from litestar.config.csrf import CSRFConfig

from config import settings

csrf_config = CSRFConfig(
    secret=settings.app.SECRET_KEY,
    exclude=["/csrf-cookie"],
    safe_methods={"GET", "HEAD", "OPTIONS"},
)
