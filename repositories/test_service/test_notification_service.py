import pytest
from services.notification_service import NotificationService
from repositories.in_memory.notification_in_memory import InMemoryNotificationRepository
from notification import Notification

@pytest.fixture
def notification_service():
    repo = InMemoryNotificationRepository()
    return NotificationService(repo)

def test_send_and_get_notification(notification_service):
    notif = Notification(id="n1", recipient="user1", message="Hello")
    notification_service.send_notification(notif)
    result = notification_service.get_notification("n1")
    assert result.recipient == "user1"
    assert result.message == "Hello"

def test_send_invalid_notification(notification_service):
    with pytest.raises(ValueError):
        notification_service.send_notification(Notification(id="n2", recipient="", message=""))

def test_list_notifications(notification_service):
    notification_service.send_notification(Notification(id="n1", recipient="user1", message="Hello"))
    notification_service.send_notification(Notification(id="n2", recipient="user2", message="Hi"))
    assert len(notification_service.list_notifications()) == 2

def test_delete_notification(notification_service):
    notif = Notification(id="n1", recipient="user1", message="Hello")
    notification_service.send_notification(notif)
    notification_service.delete_notification("n1")
    with pytest.raises(ValueError):
        notification_service.get_notification("n1")
