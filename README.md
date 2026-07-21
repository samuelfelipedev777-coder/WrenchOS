# ⚙️ Wrench

Wrench é um sistema CLI de gerenciamento de projetos feito em Python com SQLite.

O objetivo do projeto é praticar arquitetura backend, organização de código, persistência de dados e boas práticas de desenvolvimento.

---

## 🚀 Sobre o projeto

O Wrench nasceu como um projeto de estudo prático para entender como funciona um backend simples na prática, sem frameworks.

Aqui eu trabalhei conceitos como:

- CRUD completo (Create, Read, Update, Delete)
- Organização em camadas (CLI, Repository, Database)
- Uso de SQLite como banco de dados local
- Enum para controle de status
- Validação e estruturação de fluxo de terminal
- Refatoração para código limpo e reutilizável

---

## 🧠 O que eu aprendi com esse projeto

Esse projeto foi importante para consolidar conceitos reais de backend:

- Separação de responsabilidades
- Fluxo de dados entre CLI → Repository → Database
- Manipulação de banco de dados com SQLite
- Uso de classes e objetos para representar entidades
- Estruturação de sistemas em camadas
- Refatoração e redução de repetição de código

---

## 🔐 Segurança (SQL Injection Safe)

Um dos pontos importantes implementados no projeto foi a proteção contra SQL Injection.

Todas as queries utilizam **parametrização com `?`**, garantindo que inputs do usuário não sejam interpretados como código SQL.

Exemplo:

```python
cursor.execute(
    "INSERT INTO projects (name, description, status) VALUES (?, ?, ?)",
    (name, description, status)
)