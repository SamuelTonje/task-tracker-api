from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.identity.domain.value_objects.password import Password
from app.shared.infrastructure.databases.dependencies import get_db
from app.identity.interfaces.api.schemas.register_request import RegisterRequest

from app.identity.application.commands.register_user.register_user_command import RegisterUserCommand
from app.identity.application.commands.register_user.register_user_handler import RegisterUserHandler

from app.identity.infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from app.identity.infrastructure.security.password.bcrypt_password_hasher import BcryptPasswordHasher

def register(request: RegisterRequest, db: Session = Depends(get_db)):
    try:
        user_repository = SQLAlchemyUserRepository(db)
        password_hasher = BcryptPasswordHasher()

        command = RegisterUserCommand(
            email=request.email,
            password=Password(request.password),
        )

        handler = RegisterUserHandler(user_repository, password_hasher)
        result = handler.handle(command)

        return {
            "id": result.id,
            "email": result.email,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))