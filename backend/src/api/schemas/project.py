from pydantic import BaseModel

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    status: str

class ProjectCreate(BaseModel):
    name: str
    description: str
    status: str

class ProjectUpdate(BaseModel):
    status: str