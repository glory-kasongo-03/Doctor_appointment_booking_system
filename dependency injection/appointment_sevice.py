# services/appointment_service.py
from typing import List
from appointment import Appointment
from repositories.i_appointment_repository import IAppointmentRepository

class AppointmentService:
    def __init__(self, repository: IAppointmentRepository):
        self._repository = repository

    def schedule(self, appointment: Appointment) -> None:
        self._repository.add(appointment)

    def cancel(self, appointment_id: int) -> None:
        self._repository.delete(appointment_id)

    def get_patient_appointments(self, patient_id: int) -> List[Appointment]:
        return self._repository.find_by_patient_id(patient_id)

    def get_doctor_appointments(self, doctor_id: int) -> List[Appointment]:
        return self._repository.find_by_doctor_id(doctor_id)
