from src.projects.repository import ProjectRepository
from fastapi import HTTPException
import logging

class ProjectService:
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def create_project(self, project):
        if not project.name or not project.name.strip():
            raise ValueError("O nome do projeto não pode estar vazio.")
        logging.info(f"Projeto criado e validado com sucesso: {project.name}")
        return self.repository.create(project)

    def list_projects(self):
        return self.repository.list_all()

    def find_project(self, project_id):
        project = self.repository.find_project_by_id(project_id)

        if project is None:
            raise HTTPException(
                status_code=404,
                detail="Projeto não encontrado."
            )
        return project
    
    def update_project(self, project_id, project_update):
        existing_project = self.repository.find_project_by_id(project_id)

        if existing_project is None:
            raise HTTPException(
                status_code=404,
                detail="Projeto não encontrado."
            )
        return self.repository.update_project_status(project_id, project_update.status)

    def delete_project(self, project_id):
        deleted = self.repository.delete_project(project_id)

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Projeto não encontrado."
            )
        return