from repositories.i_notification_repository import INotificationRepository
from notification import Notification

class NotificationService:
    def __init__(self, repository: INotificationRepository):
        self._repository = repository

    def send_notification(self, notification: Notification):
        if not notification.recipient or not notification.message:
            raise ValueError("Notification must have a recipient and message")
        self._repository.save(notification)

    def get_notification(self, notification_id: str) -> Notification:
        notif = self._repository.find_by_id(notification_id)
        if not notif:
            raise ValueError("Notification not found")
        return notif

    def list_notifications(self):
        return self._repository.find_all()

    def delete_notification(self, notification_id: str):
        if not self._repository.find_by_id(notification_id):
            raise ValueError("Cannot delete non-existent notification")
        self._repository.delete(notification_id)
