# repositories/__init__.py

__all__ = [
    # Interfaces
    "IPatientRepository", "IDoctorRepository", "IAppointmentRepository",
    "IAdminRepository", "INotificationRepository",

    # In-memory Implementations
    "InMemoryPatientRepository", "InMemoryDoctorRepository",
    "InMemoryAppointmentRepository", "InMemoryAdminRepository",
    "InMemoryNotificationRepository",

    # Services
    "PatientService", "DoctorService", "AppointmentService",
    "AdminService", "NotificationService"
]

# Interfaces
from i_patient_repository import IPatientRepository
from i_doctor_repository import IDoctorRepository
from i_appointment_repository import IAppointmentRepository
from i_admin_repository import IAdminRepository
from i_notification_repository import INotificationRepository

# In-memory Repositories
from .in_memory.patient_in_memory import InMemoryPatientRepository
from .in_memory.doctor_in_memory import InMemoryDoctorRepository
from .in_memory.appointment_in_memory import InMemoryAppointmentRepository
from .in_memory.admin_in_memory import InMemoryAdminRepository
from .in_memory.notification_in_memory import InMemoryNotificationRepository

# Services (assuming they are located in a sibling services/ folder)
from services.patient_service import PatientService
from services.doctor_service import DoctorService
from services.appointment_service import AppointmentService
from services.admin_service import AdminService
from services.notification_service import NotificationService

