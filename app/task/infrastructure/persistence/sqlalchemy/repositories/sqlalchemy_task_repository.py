from typing import Optional

from sqlalchemy.orm import Session

from app.identity.domain.value_objects.user_id import UserId
from app.old.domain.value_objects.task_status import TaskStatus
from app.task.domain.repositories.task_repository_interface import TaskRepositoryInterface
from app.task.domain.value_objects.task import Task
from app.task.domain.value_objects.task_id import TaskId
from app.task.domain.value_objects.task_title import TaskTitle
from app.task.infrastructure.persistence.sqlalchemy.models.task_model import TaskModel


class SQLAlchemyTaskRepository(TaskRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def find(self, user_id: UserId, task_id: TaskId) -> Optional[Task]:
        task_model = self.db.query(TaskModel).filter(TaskModel.id == task_id, TaskModel.user_id == user_id).first()
        
        if not task_model:
            return None
        
        return Task(
            TaskId(task_model.id), 
            TaskTitle(task_model.title), 
            TaskStatus(task_model.status),
            UserId(task_model.user_id),
            task_model.description
        )
    
    def save(self, task:Task) -> Task:
        task_model = TaskModel(
            id = task.id.value,
            title = task.title.value,
            status = task.status.value,
            user_id = task.user_id.value,
            description = task.description
        )

        self.db.add(task_model)
        self.db.commit()
        self.db.refresh(task_model)

        return task
    
    def find_many(self, user_id: UserId, title: str, status: Optional[str] = None) -> tuple[list[Task], int]:
        pass

    def update(self, task: Task) -> Task:
        pass

    def delete(self, task: Task) -> Task:
        pass