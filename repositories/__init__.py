# repositories/__init__.py

# Explicitly define what should be exported when using `from repositories import *`
__all__ = [
    "IPatientRepository", "IDoctorRepository", "IAppointmentRepository",
    "INotificationRepository", "IAdminRepository",
    "Patient_InMemory", "Doctor_InMemory",
    "Appointment_InMemory", "Notification_InMemory",
    "Admin_InMemory"
]

# Import the specific components to make them accessible through the package
from .IPatientRepository import IPatientRepository
from .IDoctorRepository import IDoctorRepository
from .IAppointmentRepository import IAppointmentRepository
from .INotificationRepository import INotificationRepository
from .IAdminRepository import IAdminRepository

from .inmemory.Patient_InMemory import InMemoryPatientRepository
from .inmemory.Doctor_InMemory import InMemoryDoctorRepository
from .inmemory.Appointment_InMemory import InMemoryAppointmentRepository
from .inmemory.Notification_InMemory import InMemoryNotificationRepository
from .inmemory.Admin_InMemory import InMemoryAdminRepository
