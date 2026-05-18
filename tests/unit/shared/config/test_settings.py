from app.shared.infrastructure.config.settings import settings

def test_settings_loaded():
    assert settings.DATABASE_URL is not None
    assert settings.JWT_SECRET_KEY is not None
    assert settings.JWT_ALGORITHM is not None
    assert settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES is not None
    assert settings.APP_NAME == "Task Tracker API"

    assert isinstance(settings.DATABASE_URL, str)
    assert isinstance(settings.JWT_SECRET_KEY, str)
    assert isinstance(settings.JWT_ALGORITHM, str)
    assert isinstance(settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES, int)