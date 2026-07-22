
from typing import Optional

from app.identity.domain.repositories.user_repository_interface import UserRepositoryInterface
from app.task.application.queries.get_task.get_task_query import GetTaskQuery
from app.task.domain.repositories.task_repository_interface import TaskRepositoryInterface
from app.task.domain.value_objects.task import Task


class GetTaskHandler:
    def __init__(self, user_repository: UserRepositoryInterface, task_repository: TaskRepositoryInterface):
        self.user_repository = user_repository
        self.task_repository = task_repository

    def handle(self, query: GetTaskQuery) -> Optional[Task]:
        existing_user = self.user_repository.find(query.user_id)
        if not existing_user:
            raise Exception("User does not exist")
        
        return self.task_repository.find(query.user_id, query.task_id)
