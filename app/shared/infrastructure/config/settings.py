from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Task Tracker API"
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

