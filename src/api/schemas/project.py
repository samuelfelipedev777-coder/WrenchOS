from pydantic import BaseModel

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    status: str