import logfire
from app.config import settings

def setup_logging(app=None):
    logfire.configure(
        token=settings.LOGFIRE_TOKEN,
        service_name="axiom-api",
        environment=settings.ENVIRONMENT
    )
    if app is not None:
        logfire.instrument_fastapi(app)
    logfire.instrument_sqlalchemy()


    