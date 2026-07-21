from fastapi import APIRouter

from app.task.interfaces.api.controllers.create_task_controller import create
from app.task.interfaces.api.controllers.get_task_controller import get

taskRouter = APIRouter(prefix="/tasks", tags=["public"],)

taskRouter.add_api_route("/create", create, methods=["POST"])
taskRouter.add_api_route("/get/{task_id}", get, methods=["GET"])
