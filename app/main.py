from fastapi import FastAPI

from app.shared.infrastructure.config.settings import settings
from app.shared.infrastructure.web.exception_handlers import register_exception_handlers
from app.identity.interfaces.api.routers.auth_router import privateRouter, publicRouter
from app.task.interfaces.api.routers.task_router import taskRouter

app = FastAPI(
    title=settings.APP_NAME,
)

app.include_router(
    prefix="/api/v1",
    router=privateRouter,
)

app.include_router(
    prefix="/api/v1",
    router=publicRouter,
)

app.include_router(
    prefix="/api/v1",
    router=taskRouter,
)

register_exception_handlers(app)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
    }
