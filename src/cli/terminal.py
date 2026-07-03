from src.cli.menu import show_menu
from src.projects.repository import ProjectRepository
from src.database.database import Database
from src.projects.project import Project
from src.projects.status import ProjectStatus

# Evita repetir o input do ID e a validação do banco nas opções 3 e 4 (clean code sempre!)
def get_and_validate_project(repository):
    project_id = input("Insira o id do projeto que deseja buscar: ")
    projects = repository.find_project_by_id(project_id)
    
    if not projects:
        print("Nenhum projeto encontrado...")
        return None, None
    return project_id, projects

# Evita poluir o fluxo da opção 4 com textos estáticos de interface
def show_menu_project_status():
    print("Escolha o novo status:")
    print("1 - IDEIA")
    print("2 - PLANEJANDO")
    print("3 - EM DESENVOLVIMENTO")
    print("4 - PAUSADO")
    print("5 - CONCLUÍDO")
    print("6 - ARQUIVADO")
    return input("Selecione um dentre os status para realizar a alteração: ")

# Gerencia o fluxo principal do terminal de forma limpa e modular
def run_terminal():
    database = Database()
    database.connect()
    repository = ProjectRepository(database)

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
        
        if option == "1":
            project_name = input("Digite o nome do projeto: ")
            project_description = input("Digite a descrição: ")
            project = Project(project_name, project_description)
            repository.create(project)
        
        elif option == "2":
            projects = repository.list_all()
            if not projects:
                print("Nenhum projeto encontrado...")
            else:
                for project in projects:
                    print(project[1])
        
        elif option == "3":
            # Reaproveitando a função auxiliar de busca e validação mantendo limpo sempre
            _, projects = get_and_validate_project(repository)
            if projects:
                for project in projects:
                    print(project)
        
        elif option == "4":
            # Mais um reaproveitamento para organização
            project_id, projects = get_and_validate_project(repository)
            if not projects:
                continue
            
            status_option = show_menu_project_status()

            if status_option in status_map:
                selected_status = status_map[status_option]
                repository.update_project_status(project_id, selected_status.value)
                print("Status atualizado com sucesso!")
            else:
                print("Opção de status inválida.")
        
        elif option == "5":
            project_id, projects = get_and_validate_project(repository)
            if projects:
                repository.delete_project(project_id)
                print("Projeto deletado com sucesso!")
        
        elif option == "0":
            print("Encerrando o Wrench...")
            return