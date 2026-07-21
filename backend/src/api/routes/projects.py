from fastapi import APIRouter, Depends
from src.services.project_service import ProjectService
from src.api.dependencies import get_project_service
from src.api.schemas.project import ProjectResponse, ProjectCreate

router = APIRouter()

@router.get("/projects", response_model=list[ProjectResponse])
async def list_projects(service: ProjectService = Depends(get_project_service)):
    return service.list_projects()

@router.get("/projects/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: int, service: ProjectService = Depends(get_project_service)):
    return service.find_project(project_id)

@router.post("/projects", response_model=ProjectResponse)
async def create_project(project: ProjectCreate, service: ProjectService = Depends(get_project_service)):
    return service.create_project(project)

@router.put("/projects/{project_id}", response_model=ProjectResponse)
async def update_project_status(project_id: int, project: ProjectCreate, service: ProjectService = Depends(get_project_service)):
    return service.update_project(project_id, project)

@router.delete("/projects/{project_id}", status_code=204)
async def delete_project(project_id: int, service: ProjectService = Depends(get_project_service)):
    service.delete_project(project_id)