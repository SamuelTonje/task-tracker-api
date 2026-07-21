from app.identity.domain.value_objects.user_id import UserId

class CreateTaskCommand:
    def __init__(self, user_id: str, description: str, title: str, status: str):
        self.user_id = user_id
        self.description = description
        self.title = title
        self.status = status