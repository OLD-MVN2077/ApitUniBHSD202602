# API RESTful em Camadas (FastAPI + SQLite) - Projeto A4

Esta API foi organizada em múltiplas camadas: `database.py` contém a conexão e criação das tabelas, `models.py` define os contratos Pydantic e `main.py` inicializa o FastAPI e declara as rotas.

Esta é uma API educacional desenvolvida em Python com o framework **FastAPI** e banco de dados relacional **SQLite**. Ela atende aos requisitos iniciais de persistência de dados e documentação automática, servindo como backend para integração com a UC de Usabilidade.

## 🛠 Tecnologias e Pré-requisitos

* **Python 3.8+**
* **uv** (Gerenciador de pacotes e projetos ultrarrápido para Python)
* **FastAPI** (Framework web de alta performance)
* **Uvicorn** (Servidor web ASGI)
* **SQLite** (Banco de dados relacional nativo do Python)

## ⚙️ Como configurar e executar (usando `uv`)

1. Clone este repositório para o seu ambiente local (ou abra no GitHub Codespaces).
2. No terminal, dentro da pasta do projeto, instale o **uv**
```bash
pip install uv
```
3. No terminal, dentro da pasta do projeto, inicialize o ambiente com o **uv** (isso criará o `pyproject.toml` e preparará o ambiente virtual isolado):
   ```bash
   uv init
   ```
4. Adicione as dependências do projeto. O **uv** fará o download e a instalação em frações de segundo:
   ```bash
   uv add fastapi uvicorn
   ```
5. Inicie o servidor local da API utilizando o comando `run` do **uv**:
   ```bash
   uv run uvicorn main:app --reload
   ```
   *(Na primeira execução, o banco de dados será criado automaticamente na mesma pasta).*

6. O servidor estará rodando em: `http://127.0.0.1:8000`

## 📖 Documentação e Testes (Swagger UI)

A API possui documentação interativa gerada automaticamente. Você não precisa de ferramentas externas como Postman ou Insomnia para testar as rotas.

Com o servidor em execução, acesse no navegador:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

## 🚀 Resumo dos Endpoints Disponíveis

A API implementa o CRUD completo. Todos os endpoints estão definidos no arquivo `main.py`:

* **POST `/registros`**: Cria um novo registro no banco (Status `201 Created` ou `400 Bad Request`).
* **GET `/registros`**: Retorna a lista com todos os registros salvos (Status `200 OK`).
* **GET `/registros/{id}`**: Busca os detalhes de um registro específico (Status `200 OK` ou `404 Not Found`).
* **PUT `/registros/{id}`**: Atualiza os dados de um registro existente (Status `200 OK` ou `404 Not Found`).
* **DELETE `/registros/{id}`**: Exclui um registro do banco de dados (Status `200 OK` ou `404 Not Found`).

O ponto de entrada ASGI da aplicação é `main:app`.
