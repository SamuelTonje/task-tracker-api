from fastapi import Depends
from sqlalchemy.orm import Session

from app.identity.infrastructure.persistence.sqlalchemy.models.user_model import UserModel
from app.identity.infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from app.identity.interfaces.api.deps.auth_dependency import get_current_user
from app.shared.infrastructure.databases.dependencies import get_db
from app.task.application.queries.get_task.get_task_handler import GetTaskHandler
from app.task.application.queries.get_task.get_task_query import GetTaskQuery
from app.task.infrastructure.persistence.sqlalchemy.repositories.sqlalchemy_task_repository import SQLAlchemyTaskRepository
from app.task.interfaces.api.schemas.get_task_request import GetTaskRequest


def get(request: GetTaskRequest = Depends(), current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    user_repository = SQLAlchemyUserRepository(db)
    task_repository = SQLAlchemyTaskRepository(db)

    query = GetTaskQuery(current_user.id, request.task_id)
    handler = GetTaskHandler(user_repository, task_repository)

    task = handler.handle(query)

    return task