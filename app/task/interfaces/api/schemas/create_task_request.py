from pydantic import BaseModel

class CreateTaskRequest(BaseModel):
    description: str
    title: str 
    status: str