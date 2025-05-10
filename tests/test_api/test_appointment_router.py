import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_appointment():
    response = client.post("/appointments", json={"id": "a1", "patient_id": "p1", "doctor_id": "d1"})
    assert response.status_code == 200

def test_get_all_appointments():
    response = client.get("/appointments")
    assert response.status_code == 200

def test_get_appointment_by_id():
    response = client.get("/appointments/a1")
    assert response.status_code == 200

def test_update_appointment():
    response = client.put("/appointments/a1", json={"id": "a1", "patient_id": "p1", "doctor_id": "d2"})
    assert response.status_code == 200

def test_delete_appointment():
    response = client.delete("/appointments/a1")
    assert response.status_code == 204