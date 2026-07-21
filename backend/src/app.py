from src.database.database import Database

class App:
    def start(self):
        print("Inicializando o Wrench...")
        database = Database()
        database.connect()
        database.create_tables()