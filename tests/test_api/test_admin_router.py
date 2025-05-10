import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_admin():
    response = client.post("/admins", json={"id": "a1", "username": "admin1"})
    assert response.status_code == 200

def test_get_all_admins():
    response = client.get("/admins")
    assert response.status_code == 200

def test_get_admin_by_id():
    response = client.get("/admins/a1")
    assert response.status_code == 200

def test_update_admin():
    response = client.put("/admins/a1", json={"id": "a1", "username": "updatedadmin"})
    assert response.status_code == 200

def test_delete_admin():
    response = client.delete("/admins/a1")
    assert response.status_code == 204
