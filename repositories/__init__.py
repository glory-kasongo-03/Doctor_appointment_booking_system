# repositories/__init__.py

# Explicitly define what should be exported when using `from repositories import *`
__all__ = [
    "i_patient_repository", "i_doctor_repository", "i_appointment_repository",
    "i_notification_repository", "i_admin_repository",
    "patient_in_memory", "doctor_in_memory",
    "appointment_in_memory", "notification_in_memory",
    "admin_in_memory"
]

# Import the specific components to make them accessible through the package

# Import the repository interfaces
from .repository_interface_design import IRepository
from repositories import i_admin_repository
from repositories import i_patient_repository
from repositories import i_doctor_repository
from repositories import i_appointment_repository
from repositories import i_notification_repository

# Import the repository interfaces
from .i_patient_repository import IPatientRepository
from .i_doctor_repository import IDoctorRepository
from .i_appointment_repository import IAppointmentRepository
from .i_notification_repository import INotificationRepository
from .i_admin_repository import IAdminRepository

# Import the in-memory implementations
from .in_memory import patient_in_memory
from .in_memory import doctor_in_memory
from .in_memory import appointment_in_memory
from .in_memory import notification_in_memory
from .in_memory import admin_in_memory
