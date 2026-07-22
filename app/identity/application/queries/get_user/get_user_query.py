from app.identity.domain.value_objects.user_id import UserId

class GetUserQuery:
    def __init__(self, id: UserId):
        self.id = id
        pass