from fastapi import FastAPI

from app.shared.infrastructure.config.settings import settings
from app.shared.infrastructure.web.exception_handlers import register_exception_handlers

app = FastAPI(
    title=settings.APP_NAME,
)

register_exception_handlers(app)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
    }
