from abc import ABC, abstractmethod

from app.identity.domain.entities.users import User

class UserRepositoryInterface(ABC):
    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass