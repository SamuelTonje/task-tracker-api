from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.identity.application.queries.get_user.get_user_handler import GetUserHandler
from app.identity.application.queries.get_user.get_user_query import GetUserQuery
from app.identity.domain.value_objects.user_id import UserId
from app.identity.infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from app.identity.interfaces.api.deps.auth_dependency import get_current_user

from app.identity.infrastructure.persistence.sqlalchemy.models.user_model import UserModel
from app.identity.interfaces.api.schemas.get_user_request import GetUserRequest
from app.shared.infrastructure.databases.dependencies import get_db

def get_user(request: GetUserRequest = Depends(), db: Session = Depends(get_db)):
    user_repository = SQLAlchemyUserRepository(db)
    query = GetUserQuery(UserId(request.id))
    handler = GetUserHandler(user_repository)
    try:
        current_user = handler.handle(query)
    except Exception as e:
        raise HTTPException(status_code=404, detail="User not found") from e
    
    return {
        "id": current_user.id,
        "email": current_user.email,
    }