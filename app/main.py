from fastapi import FastAPI

from app.shared.infrastructure.config.settings import settings
from app.shared.infrastructure.web.exception_handlers import register_exception_handlers
from app.identity.interfaces.api.routers.auth_router import router as auth_router

app = FastAPI(
    title=settings.APP_NAME,
)

app.include_router(
    prefix="/api/v1",
    router=auth_router,
)

register_exception_handlers(app)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
    }
