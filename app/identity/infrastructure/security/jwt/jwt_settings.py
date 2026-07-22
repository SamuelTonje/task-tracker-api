from app.shared.infrastructure.config.settings import settings


class JWTSettings:
    SECRET_KEY = settings.JWT_SECRET_KEY
    ALGORITHM = settings.JWT_ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES = settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES