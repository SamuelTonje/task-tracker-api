from fastapi import Depends

from app.identity.interfaces.api.deps.auth_dependency import get_current_user

from app.identity.infrastructure.persistence.sqlalchemy.models.user_model import UserModel

def me(current_user: UserModel = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
    }