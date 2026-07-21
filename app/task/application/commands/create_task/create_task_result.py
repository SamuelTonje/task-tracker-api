from app.task.domain.value_objects.task import Task


class CreateTaskResult:
    def __init__(self, task: Task):
        self.task = task