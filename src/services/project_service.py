from src.projects.repository import ProjectRepository
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
        return self.repository.find_project_by_id(project_id)
    
    def update_project(self, project_id, new_status):
        return self.repository.update_project_status(project_id, new_status)

    def delete_project(self, project_id):
        return self.repository.delete_project(project_id)