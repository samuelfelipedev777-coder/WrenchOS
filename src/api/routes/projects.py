from fastapi import APIRouter, Depends
from src.services.project_service import ProjectService
from src.api.dependencies import get_project_service
from src.api.schemas.project import ProjectResponse

router = APIRouter()

@router.get("/projects", response_model=list[ProjectResponse])
async def list_projects(service: ProjectService = Depends(get_project_service)):
    return service.list_projects()