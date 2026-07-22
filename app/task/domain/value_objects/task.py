from app.identity.domain.value_objects.user_id import UserId
from app.old.domain.value_objects.task_status import TaskStatus
from app.task.domain.value_objects.task_id import TaskId
from app.task.domain.value_objects.task_title import TaskTitle

class Task:
    def __init__(self, id: TaskId, title: TaskTitle, status: TaskStatus, user_id: UserId, description: str):
        self.id = id
        self.title = title
        self.status = status
        self.user_id = user_id
        self.description = description