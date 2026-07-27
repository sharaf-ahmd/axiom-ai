import logfire
from app.config import settings

def setup_logging():

    logfire.configure(
        token=settings.LOGFIRE_TOKEN,
        service_name="axiom-api",
        environment=settings.ENVIRONMENT
    )

    logfire.instrument_fastapi()
    logfire.instrument_sqlalchemy()