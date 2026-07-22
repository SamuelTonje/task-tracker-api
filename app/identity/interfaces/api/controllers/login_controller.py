from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.shared.infrastructure.databases.dependencies import get_db
from app.shared.infrastructure.config.settings import settings

from app.identity.interfaces.api.schemas.login_request import LoginRequest

from app.identity.infrastructure.security.jwt.jwt_service import JWTService

from app.identity.infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from app.identity.infrastructure.security.password.bcrypt_password_hasher import BcryptPasswordHasher

from app.identity.application.commands.login_user.login_user_command import LoginUserCommand
from app.identity.application.commands.login_user.login_user_handler import LoginUserHandler

def login(request: LoginRequest, db: Session = Depends(get_db)):
    try:
        user_repository = SQLAlchemyUserRepository(db)
        password_hasher = BcryptPasswordHasher()
        jwt_service = JWTService(
            settings.JWT_SECRET_KEY, 
            settings.JWT_ALGORITHM, 
            settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )

        command = LoginUserCommand(
            email=request.email,
            password=request.password,
        )

        handler = LoginUserHandler(user_repository, password_hasher, jwt_service)
        result = handler.handle(command)

        return {
            "access_token": result.access_token,
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))