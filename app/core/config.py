from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    app_env: str = "development"
    cache_ttl: int = 300

    class Config:
        env_file = ".env"

settings = Settings()
