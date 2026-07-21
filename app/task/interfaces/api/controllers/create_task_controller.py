from fastapi import Depends
from sqlalchemy.orm import Session

from app.identity.domain.value_objects.user_id import UserId
from app.identity.infrastructure.persistence.sqlalchemy.models.user_model import UserModel
from app.identity.interfaces.api.deps.auth_dependency import get_current_user
from app.shared.infrastructure.databases.dependencies import get_db
from app.task.application.commands.create_task.create_task_command import CreateTaskCommand
from app.task.application.commands.create_task.create_task_handler import CreateTaskHandler
from app.task.infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_task_repository import SQLAlchemyTaskRepository
from app.task.interfaces.api.schemas.create_task_request import CreateTaskRequest

def create(request: CreateTaskRequest, current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    command = CreateTaskCommand(
        user_id = current_user.id,
        description= request.description,
        title=request.title,
        status=request.status
    )

    task_repository = SQLAlchemyTaskRepository(db)
    handler = CreateTaskHandler(task_repository)

    task = handler.handle(command)

    return {
        "task_id": task.id,
        "user_id": task.user_id
    }

