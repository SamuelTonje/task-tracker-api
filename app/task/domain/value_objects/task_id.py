from uuid import UUID

class TaskId:
    def __init__(self, value: UUID | str):
        self.value = value if isinstance(value, UUID) else UUID(value)

    def __str__(self):
        return self.value