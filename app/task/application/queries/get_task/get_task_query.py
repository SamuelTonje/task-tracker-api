from app.identity.domain.value_objects.user_id import UserId
from app.task.domain.value_objects.task_id import TaskId

class GetTaskQuery:
    def __init__(self, user_id: UserId, task_id: TaskId):
        self.user_id = user_id
        self.task_id = task_id
