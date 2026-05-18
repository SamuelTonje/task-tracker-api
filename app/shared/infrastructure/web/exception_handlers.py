from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.shared.domain.exceptions.not_found_exception import NotFoundException
from app.shared.domain.exceptions.unauthorized_exception import UnauthorizedException
from app.shared.domain.exceptions.validation_exception import ValidationException

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(NotFoundException)
    async def not_found_exception_handler(_, exc: NotFoundException):
        return JSONResponse(
            status_code=404,
            content={"detail": str(exc)},
        )

    @app.exception_handler(ValidationException)
    async def validation_exception_handler(_, exc: ValidationException):
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc)},
        )

    @app.exception_handler(UnauthorizedException)
    async def unauthorized_exception_handler(_, exc: UnauthorizedException):
        return JSONResponse(
            status_code=401,
            content={"detail": str(exc)},
        )