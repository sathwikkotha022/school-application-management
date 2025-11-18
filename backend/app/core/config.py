from pydantic_settings import BaseSettings

class Settings(BaseSettings):
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

    class Config:
        env_file = ".env"

settings = Settings()
