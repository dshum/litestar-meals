import sentry_sdk

from config import settings


def on_startup() -> None:
    sentry_sdk.init(
        dsn=settings.sentry.DSN,
        environment=settings.app.ENVIRONMENT,
        release=settings.app.BUILD_NUMBER,
        integrations=[],
        traces_sample_rate=settings.sentry.TRACES_SAMPLE_RATE,
        enable_tracing=settings.sentry.ENABLE,
    )
