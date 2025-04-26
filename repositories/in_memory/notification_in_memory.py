from typing import Dict
from repositories.i_notification_repository import INotificationRepository,Notification

class InMemoryNotificationRepository(INotificationRepository):
    def __init__(self):
        self._notifications: Dict[str, Notification] = {}

    def save(self, notification: Notification) -> None:
        self._notifications[notification.id] = notification

    def find_by_id(self, id: str) -> Notification:
        return self._notifications.get(id)

    def find_all(self) -> list[Notification]:
        return list(self._notifications.values())

    def delete(self, id: str) -> None:
        if id in self._notifications:
            del self._notifications[id]
