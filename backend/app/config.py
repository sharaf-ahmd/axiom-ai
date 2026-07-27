from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Axiom AI"

    ENVIRONMENT: str

    DATABASE_URL: str

    REDIS_URL: str

    LOGFIRE_TOKEN: str

    JWT_SECRET: str

    JWT_ALGORITHM: str = "HS256"


    class Config:
        env_file = ".env"


settings = Settings()