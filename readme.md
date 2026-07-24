# To-Do API — Projeto DevOps

API simples (Flask) usada como veículo de aprendizagem para Docker, Jenkins CI/CD e Kubernetes.

## Endpoints

- `GET /health` — healthcheck
- `GET /tasks` — lista tarefas
- `POST /tasks` — cria tarefa (`{"title": "..."}`)
- `DELETE /tasks/<id>` — apaga tarefa

## Correr localmente

\`\`\`bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app/main.py
\`\`\`

## Correr com Docker

\`\`\`bash
docker pull gilmartins2004/todo-api:v1
docker run -d -p 5000:5000 gilmartins2004/todo-api:v1
\`\`\`