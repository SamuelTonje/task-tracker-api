from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.shared.infrastructure.databases.dependencies import get_db
from app.shared.infrastructure.config.settings import settings

from app.identity.infrastructure.security.jwt.jwt_service import JWTService
from app.identity.infrastructure.persistence.sqlalchemy.models.user_model import UserModel

security = HTTPBearer()

jwt_service = JWTService(
    settings.JWT_SECRET_KEY, 
    settings.JWT_ALGORITHM, 
    settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
)

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security), 
    db: Session = Depends(get_db)
) -> UserModel:
    token = credentials.credentials
    try:
        payload = jwt_service.decode_access_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(token)}") from e

    user = db.query(UserModel).filter(UserModel.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user