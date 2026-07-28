# To-Do API — Projeto DevOps

API simples (Flask) usada como veículo de aprendizagem prática para Docker, Jenkins CI/CD e Kubernetes.

O foco deste projeto não é a aplicação em si — é a infraestrutura e automação à sua volta.

## Stack

- **Aplicação:** Python / Flask
- **Testes:** pytest
- **Containerização:** Docker (multi-stage build, non-root user) + Docker Compose
- **CI/CD:** Jenkins (Pipeline as Code via Jenkinsfile)
- **Registo de imagens:** Docker Hub

## Endpoints

| Método | Rota           | Descrição                          |
|--------|----------------|-------------------------------------|
| GET    | `/health`      | Healthcheck                         |
| GET    | `/tasks`       | Lista todas as tarefas              |
| POST   | `/tasks`       | Cria tarefa — body: `{"title": "..."}` |
| DELETE | `/tasks/<id>`  | Apaga uma tarefa pelo id            |

## Correr localmente (sem Docker)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app/main.py
```

## Correr com Docker Compose (recomendado)

```bash
docker compose up -d
```

A API fica disponível em `http://localhost:5000`.

## Correr a imagem publicada, sem clonar o repositório

```bash
docker pull gilmartins2004/todo-api:latest
docker run -d -p 5000:5000 gilmartins2004/todo-api:latest
```

## Correr os testes

```bash
pytest
```

## Pipeline CI/CD (Jenkins)

O `Jenkinsfile` na raiz do projeto define um pipeline que, a cada execução:

1. Faz checkout do código
2. Instala dependências e corre a suite de testes (`pytest`)
3. Se os testes passarem, constrói a imagem Docker
4. Publica a imagem no Docker Hub, com tag de build (`vN`) e `latest`

O pipeline falha e para em qualquer etapa que não passe — nenhuma imagem quebrada chega ao Docker Hub.

## Estrutura do projeto

```
.
├── app/                # código da aplicação
│   ├── __init__.py
│   └── main.py
├── tests/               # testes automatizados
│   └── test_app.py
├── conftest.py          # configuração do pytest (path resolution)
├── Dockerfile            # receita da imagem (multi-stage, non-root)
├── docker-compose.yaml   # orquestração local
├── Jenkinsfile            # pipeline CI/CD
├── requirements.txt
└── README.md
```

