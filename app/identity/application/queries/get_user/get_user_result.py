from app.identity.domain.value_objects.user_id import UserId

class GetUserResult:
    def __init__(self, id: UserId, email: str):
        self.id = id
        self.email = email
        pass