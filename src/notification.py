from datetime import datetime

class Notification:
    def __init__(self, notification_id: str, message: str, status: str, timestamp: datetime):
        self.notification_id = notification_id
        self.message = message
        self.status = status
        self.timestamp = timestamp

    def send(self):
        print(f"Notification {self.notification_id} sent: {self.message}")

    def mark_as_read(self):
        self.status = "Read"
        print(f"Notification {self.notification_id} marked as read.")
