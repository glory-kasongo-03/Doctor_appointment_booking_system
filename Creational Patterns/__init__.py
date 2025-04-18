# creational_patterns/__init__.py

# Explicitly define what should be exported when using `from creational_patterns import *`
__all__ = [
    "UserFactory", "Patient", "Doctor", "Admin",
    "EmailNotificationFactory", "SMSNotificationFactory",
    "WebUIFactory", "MobileUIFactory",
    "AppointmentBuilder", "Report", "DatabaseConnection"
]

# Import the specific components to make them accessible through the package
from .simple_factory import UserFactory, Patient, Doctor, Admin
from .factory_method import EmailNotificationFactory, SMSNotificationFactory
from .abstract_factory import WebUIFactory, MobileUIFactory
from .builder import AppointmentBuilder
from .prototype import Report
from .singleton import DatabaseConnection
