import pytest
from repositories.in_memory.notification_in_memory import InMemoryNotificationRepository, Notification

@pytest.fixture
def repo():
    return InMemoryNotificationRepository()

def test_save_and_find_by_id(repo):
    n = Notification(id="n1", message="Test")
    repo.save(n)
    assert repo.find_by_id("n1").message == "Test"

def test_find_all(repo):
    repo.save(Notification(id="n1", message="A"))
    repo.save(Notification(id="n2", message="B"))
    assert len(repo.find_all()) == 2

def test_delete(repo):
    repo.save(Notification(id="n1", message="Delete Me"))
    repo.delete("n1")
    assert repo.find_by_id("n1") is None
