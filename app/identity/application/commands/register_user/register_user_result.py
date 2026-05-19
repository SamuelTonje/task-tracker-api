from uuid import UUID

class RegisterUserResult:
    def __init__(self, id: UUID, email: str):
        self.id = id
        self.email = email