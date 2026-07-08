from pydantic import BaseModel

class GetUserRequest(BaseModel):
    id: str