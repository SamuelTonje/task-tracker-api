from abc import ABC, abstractmethod

from app.identity.domain.entities.user import User
from app.identity.domain.value_objects.user_id import UserId

class UserRepositoryInterface(ABC):
    @abstractmethod
    def find(self, id: UserId) -> User | None:
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass