from uuid import uuid4

from app.identity.domain.repositories.user_repository_interface import UserRepositoryInterface
from app.identity.domain.value_objects.user_id import UserId
from app.old.domain.value_objects.task_status import TaskStatus
from app.task.application.commands.create_task.create_task_command import CreateTaskCommand
from app.task.application.commands.create_task.create_task_result import CreateTaskResult
from app.task.domain.repositories.task_repository_interface import TaskRepositoryInterface
from app.task.domain.value_objects.task import Task
from app.task.domain.value_objects.task_id import TaskId
from app.task.domain.value_objects.task_title import TaskTitle


class CreateTaskHandler:
    def __init__(self, task_repository:TaskRepositoryInterface):
        self.task_repository = task_repository

    def handle(self, command: CreateTaskCommand) -> Task:
        task = Task(TaskId(uuid4()), TaskTitle(command.title), TaskStatus(command.status), UserId(command.user_id), command.description)
        return self.task_repository.save(task)