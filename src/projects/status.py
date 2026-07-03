from enum import Enum

class ProjectStatus(Enum):
    IDEA = "IDEIA"
    PLANNING = "PLANEJANDO"
    DEVELOPMENT = "EM DESENVOLVIMENTO"
    PAUSED = "PAUSADO"
    COMPLETED = "COMPLETO"
    ARCHIVED = "ARQUIVADO"