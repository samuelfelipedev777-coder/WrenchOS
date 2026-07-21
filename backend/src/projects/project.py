from src.projects.status import ProjectStatus
from datetime import datetime

class Project:
    def __init__(self, name, description):
        current_time = datetime.now()
        self.name = name
        self.description = description
        self.created_at = current_time
        self.updated_at = current_time
        self.status = ProjectStatus.IDEA
    
    def get_project_info(self):
        return f"Name: {self.name}\nDescription: {self.description}\nStatus: {self.status.value}\nCriado em: {self.created_at.strftime('%d/%m/%Y %H:%M:%S')}"
    