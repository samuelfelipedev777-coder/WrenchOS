import sqlite3
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

class Database:
    def __init__(self):
        self.connection = None

    # Garante que a pasta 'data' exista e abre conexão com o banco SQLite 'wrench.db'.
    def connect(self):
        data_path = Path(__file__).parent / "data"
        data_path.mkdir(exist_ok=True)
        database_path = data_path / "wrench.db"
        print(database_path)
        logging.info("Conectando o banco de dados SQLite")
        self.connection = sqlite3.connect(database_path)
        logging.info("Banco conectado com sucesso.")
        return self.connection
    
    # Evita manter conexões abertas desnecessariamente
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            logging.info("Conexão fechada.")
        else: 
            logging.warning("Nenhuma conexão ativa para fechar.")

    # Cria a tabela 'projects' caso não exista.
    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL   
            );
        """)
        self.connection.commit()
        logging.info("Tabela projects criada/verificada.")