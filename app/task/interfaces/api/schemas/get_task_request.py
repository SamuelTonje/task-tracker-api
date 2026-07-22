from pydantic import BaseModel

class GetTaskRequest(BaseModel):
    task_id: str