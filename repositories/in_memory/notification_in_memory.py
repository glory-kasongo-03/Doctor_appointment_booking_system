from repositories.i_notification_repository import INotificationRepository
from notification import Notification
from typing import Optional

class InMemoryNotificationRepository(INotificationRepository):
    def __init__(self):
        self._notifications: dict[str, Notification] = {}

    def save(self, notification: Notification) -> None:
        self._notifications[notification.id] = notification

    def find_by_id(self, notification_id: str) -> Optional[Notification]:
        return self._notifications.get(notification_id)

    def find_all(self) -> list[Notification]:
        return list(self._notifications.values())

    def delete(self, notification_id: str) -> None:
        self._notifications.pop(notification_id, None)