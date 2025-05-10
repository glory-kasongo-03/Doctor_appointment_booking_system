
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_patient():
    response = client.post("/patients", json={"id": "p1", "name": "Alice"})
    assert response.status_code == 200
    assert response.json()["id"] == "p1"

def test_get_all_patients():
    response = client.get("/patients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_patient_by_id():
    response = client.get("/patients/p1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

def test_update_patient():
    response = client.put("/patients/p1", json={"id": "p1", "name": "Alice Updated"})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice Updated"

def test_delete_patient():
    response = client.delete("/patients/p1")
    assert response.status_code == 204