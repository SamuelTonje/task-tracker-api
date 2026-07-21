from uuid import UUID

from app.identity.domain.value_objects.user_id import UserId

class User:
    def __init__(self, id: UserId, email: str, hashed_password: str):
        self.id = id
        self.email = email
        self.hashed_password = hashed_password