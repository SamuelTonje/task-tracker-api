from passlib.context import CryptContext
from app.identity.domain.services.password_hasher_interface import PasswordHasherInterface

class BcryptPasswordHasher(PasswordHasherInterface):
    def __init__(self):
        self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, password: str) -> str:
        return self.context.hash(password)

    def verify(self, plain_password: str, hashed_password: str) -> bool:
        return self.context.verify(plain_password, hashed_password)