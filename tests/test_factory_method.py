import unittest
from creational_patterns.factory_method import (
    EmailNotificationFactory,
    SMSNotificationFactory,
    EmailNotification,
    SMSNotification,
)

# The Factory Method pattern defines an interface for creating an object but allows subclasses to alter the type of objects that will be created. 
# It promotes loose coupling by eliminating the need to bind application-specific classes into the code.

class TestFactoryMethod(unittest.TestCase):
    def test_email_notification(self):
        factory = EmailNotificationFactory()
        notification = factory.create_notification()
        self.assertIsInstance(notification, EmailNotification)

    def test_sms_notification(self):
        factory = SMSNotificationFactory()
        notification = factory.create_notification()
        self.assertIsInstance(notification, SMSNotification)
