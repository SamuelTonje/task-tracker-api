from datetime import datetime, timedelta, UTC
from jose import JWTError, jwt
from app.identity.domain.services.token_service_interface import TokenServiceInterface

class JWTService(TokenServiceInterface):
    def __init__(self, secret_key: str, algorithm: str = "HS256", access_token_expire_minutes: int = 30):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes

    def create_access_token(self, data: dict) -> str:
        payload = data.copy()
        expire = datetime.now(UTC) + timedelta(minutes=self.access_token_expire_minutes)
        payload.update({"exp": expire})
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode_access_token(self, token: str) -> dict | None:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            return None