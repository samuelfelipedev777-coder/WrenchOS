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
            project.status.value
        ))
        connection.commit()
        logging.info("Tabela criada com sucesso!")
        
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
            SELECT * FROM projects WHERE id = ?
        """, (
            project_id,
        ))
        rows = cursor.fetchone()
        return rows

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
        connection.close()
        print("Status atualizado!")

    def delete_project(self, project_id):
        connection = self.database.connection
        cursor = connection.cursor()
        cursor.execute("""
            DELETE FROM projects WHERE id = ?
        """, (
            project_id
        ))
        connection.commit()
        connection.close()
        print("Projeto deletado conforme esperado (funcionou!)")