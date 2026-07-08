from uuid import UUID

class UserId:
    def __init__(self, value: str):
        self.value = str(UUID(value))

    def __str__(self):
        return self.value