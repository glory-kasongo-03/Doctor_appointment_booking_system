from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Email sent: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS sent: {message}")

class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass

class EmailNotificationFactory(NotificationFactory):
    def create_notification(self):
        return EmailNotification()

class SMSNotificationFactory(NotificationFactory):
    def create_notification(self):
        return SMSNotification()
