import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_doctor():
    response = client.post("/doctors", json={"id": "d1", "name": "Dr. Smith"})
    assert response.status_code == 200
    assert response.json()["id"] == "d1"

def test_get_all_doctors():
    response = client.get("/doctors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_doctor_by_id():
    response = client.get("/doctors/d1")
    assert response.status_code == 200

def test_update_doctor():
    response = client.put("/doctors/d1", json={"id": "d1", "name": "Dr. Updated"})
    assert response.status_code == 200

def test_delete_doctor():
    response = client.delete("/doctors/d1")
    assert response.status_code == 204