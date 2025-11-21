from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    model_config = ConfigDict(extra='allow')

    # Database
    DB_USER: str = "root"
    DB_PASSWORD: str = "Sathwik05"
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str = "school_db"

    DATABASE_URL: str | None = None
    DEBUG: bool = False

    # JWT settings
    SECRET_KEY: str = "Sathwik05"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

settings = Settings()
