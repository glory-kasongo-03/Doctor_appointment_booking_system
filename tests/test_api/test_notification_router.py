import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_notification():
    response = client.post("/notifications", json={"id": "n1", "message": "Your appointment is confirmed"})
    assert response.status_code == 200

def test_get_all_notifications():
    response = client.get("/notifications")
    assert response.status_code == 200

def test_get_notification_by_id():
    response = client.get("/notifications/n1")
    assert response.status_code == 200

def test_update_notification():
    response = client.put("/notifications/n1", json={"id": "n1", "message": "Updated message"})
    assert response.status_code == 200

def test_delete_notification():
    response = client.delete("/notifications/n1")
    assert response.status_code == 204