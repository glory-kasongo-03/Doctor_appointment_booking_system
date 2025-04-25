from repositories.i_notification_repository import INotificationRepository
from notification import Notification
from typing import Optional

class NotificationService:
    def __init__(self, repository: INotificationRepository):
        self._repository = repository

    def send_notification(self, notification: Notification) -> None:
        self._repository.save(notification)

    def get_notification(self, notification_id: str) -> Optional[Notification]:
        return self._repository.find_by_id(notification_id)

    def list_notifications(self) -> list[Notification]:
        return self._repository.find_all()

    def remove_notification(self, notification_id: str) -> None:
        self._repository.delete(notification_id)
