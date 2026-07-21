from src.database.database import Database
import logging

logging.basicConfig(level=logging.INFO)

class ProjectRepository:
    def __init__(self, database: Database):
        self.database = database

    def create(self, project):
        connection = self.database.connection
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO projects (name, description, status)
            VALUES (?, ?, ?)
        """, (
            project.name,
            project.description,
            project.status
        ))
        connection.commit()
        logging.info("Tabela criada com sucesso!")
        project_id = cursor.lastrowid

        return {
            "id": project_id,
            "name": project.name,
            "description": project.description,
            "status": project.status
        }
        
    def list_all(self):
        
        connection = self.database.connection
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, name, description, status FROM projects
        """)

        rows = cursor.fetchall()

        projects = []

        for project in rows:
            projects.append({
                "id": project[0],
                "name": project[1],
                "description": project[2],
                "status": project[3]
            })

        return projects

    def find_project_by_id(self, project_id):
        connection = self.database.connection
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, name, description, status
            FROM projects
            WHERE id = ?
        """, (project_id,))

        project = cursor.fetchone()

        if project is None:
            return None

        return {
            "id": project[0],
            "name": project[1],
            "description": project[2],
            "status": project[3]
        }

    def update_project_status(self, project_id, new_status):
        connection = self.database.connection
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE projects SET status = ? WHERE id = ?
        """, (
            new_status,
            project_id
        ))
        connection.commit()
        print("Status atualizado!")
        return self.find_project_by_id(project_id)

    def delete_project(self, project_id):
        connection = self.database.connection
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM projects WHERE id = ?
        """, (
            project_id
        ))
        connection.commit()
        if cursor.rowcount == 0:
            return False
        logging.info("Projeto deletado com sucesso.")
        return True