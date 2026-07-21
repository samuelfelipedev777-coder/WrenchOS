from src.database.database import Database
from src.projects.repository import ProjectRepository
from src.services.project_service import ProjectService

def get_project_service():
    database = Database()
    database.connect()

    repository = ProjectRepository(database)
    service = ProjectService(repository)
    
    return service