from abc import ABC, abstractmethod

class TokenServiceInterface(ABC):
    @abstractmethod
    def create_access_token(self, data: dict) -> str:
        pass

    @abstractmethod
    def decode_access_token(self, token: str) -> dict | None:
        pass