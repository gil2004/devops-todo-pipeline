import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_get_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_task(client):
    response = client.post("/tasks", json={"title": "Aprender Jenkins"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Aprender Jenkins"
    assert data["done"] is False
    assert "id" in data


def test_create_task_without_title(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400


def test_delete_task(client):
    # cria uma tarefa primeiro
    create_response = client.post("/tasks", json={"title": "Apagar-me"})
    task_id = create_response.get_json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200


def test_delete_nonexistent_task(client):
    response = client.delete("/tasks/9999")
    assert response.status_code == 404