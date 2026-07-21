from app.old.domain.value_objects.task_status import TaskStatus
from app.task.domain.value_objects.task_id import TaskId
from app.task.domain.value_objects.task_title import TaskTitle

class Task:
    def __init__(self, id: TaskId, title: TaskTitle, status: TaskStatus, description: str):
        self.id = id
        self.title = title
        self.status = status
        self.description = description