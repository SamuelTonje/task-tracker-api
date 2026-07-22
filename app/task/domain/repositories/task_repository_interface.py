from abc import ABC, abstractmethod
from typing import Optional

from app.identity.domain.value_objects.user_id import UserId
from app.task.domain.value_objects.task import Task
from app.task.domain.value_objects.task_id import TaskId

class TaskRepositoryInterface(ABC):
    @abstractmethod
    def save(self, task:Task) -> Task:
        pass

    @abstractmethod
    def find_many(self, user_id: UserId, title: str, status: Optional[str] = None) -> tuple[list[Task], int]:
        pass
    
    @abstractmethod
    def find(self, user_id: UserId, task_id: TaskId) -> Optional[Task]:
        pass

    @abstractmethod
    def update(self, task: Task) -> Task:
        pass

    @abstractmethod
    def delete(self, task: Task) -> Task:
        pass
