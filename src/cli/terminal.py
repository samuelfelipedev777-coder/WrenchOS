from src.cli.menu import show_menu
from src.projects.repository import ProjectRepository
from src.database.database import Database
from src.projects.project import Project
from src.projects.status import ProjectStatus
from src.services.project_service import ProjectService


def get_project(service):
    """
    Centraliza a busca de projeto pelo terminal.
    Evita repetir validações nas operações que precisam de um projeto existente.
    """
    project_id = input("Insira o id do projeto que deseja buscar: ")
    project = service.find_project(project_id)

    if not project:
        print("Nenhum projeto encontrado...")
        return None, None

    return project_id, project


def select_project_status():
    """
    Responsável apenas pela interação com o usuário
    para escolha do novo status do projeto.
    """
    print("\nEscolha o novo status:")
    print("1 - IDEIA")
    print("2 - PLANEJANDO")
    print("3 - EM DESENVOLVIMENTO")
    print("4 - PAUSADO")
    print("5 - CONCLUÍDO")
    print("6 - ARQUIVADO")

    return input("Selecione um status: ")


def run_terminal():
    """
    Controla a interface CLI do sistema.
    
    A camada de terminal não possui regras de negócio
    nem manipula diretamente o banco de dados.
    Toda operação passa pela camada Service.
    Assim nos podemos dividir as "tarefas" entre camadas de forma clara.
    """
    database = Database()
    database.connect()

    repository = ProjectRepository(database)
    service = ProjectService(repository)

    status_map = {
        "1": ProjectStatus.IDEA,
        "2": ProjectStatus.PLANNING,
        "3": ProjectStatus.DEVELOPMENT,
        "4": ProjectStatus.PAUSED,
        "5": ProjectStatus.COMPLETED,
        "6": ProjectStatus.ARCHIVED
    }

    while True:
        show_menu()
        option = input("Escolha uma opção para continuar: ")

        # Cria um novo projeto
        if option == "1":
            project_name = input("Digite o nome do projeto: ")
            project_description = input("Digite a descrição: ")

            project = Project(
                project_name,
                project_description
            )

            service.create_project(project)
            print("Projeto criado com sucesso!")

        # Lista todos os projetos que existem
        elif option == "2":
            projects = service.list_projects()

            if not projects:
                print("Nenhum projeto encontrado.")
                continue

            for project in projects:
                print(project[1])

        # Busca o projeto por ID específico
        elif option == "3":
            _, project = get_project(service)

            if project:
                for data in project:
                    print(data)

        # Atualiza o status do projeto conforme quisermos
        elif option == "4":
            project_id, project = get_project(service)

            if not project:
                continue

            status_option = select_project_status()

            if status_option not in status_map:
                print("Status inválido.")
                continue

            new_status = status_map[status_option]

            service.update_project(
                project_id,
                new_status.value
            )

            print("Status atualizado com sucesso!")

        # Remove o projeto (até do banco de dados!)
        elif option == "5":
            project_id, project = get_project(service)

            if project:
                service.delete_project(project_id)
                print("Projeto removido com sucesso!")

        # Encerra a aplicação
        elif option == "0":
            print("Encerrando o Wrench...")
            return