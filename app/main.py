from flask import Flask, request, jsonify

app = Flask(__name__)

# "Base de dados" em memória (mais tarde substituímos por PostgreSQL)
tasks = []
next_id = 1


@app.route("/health", methods=["GET"])
def health():
    """Usado pelo Docker/Kubernetes para saber se a app está viva."""
    return jsonify({"status": "ok"}), 200


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """Devolve todas as tarefas."""
    return jsonify(tasks), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    """Cria uma nova tarefa. Espera JSON: {"title": "Comprar leite"}"""
    global next_id

    data = request.get_json(silent=True)
    if not data or "title" not in data:
        return jsonify({"error": "O campo 'title' é obrigatório"}), 400

    task = {
        "id": next_id,
        "title": data["title"],
        "done": False,
    }
    tasks.append(task)
    next_id += 1

    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Apaga uma tarefa pelo id."""
    global tasks

    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": f"Tarefa {task_id} apagada"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)