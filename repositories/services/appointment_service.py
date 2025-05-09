from repositories.i_appointment_repository import IAppointmentRepository
from repositories.i_patient_repository import IPatientRepository
from repositories.i_doctor_repository import IDoctorRepository
from appointment import Appointment

class AppointmentService:
    def __init__(self, appointment_repo: IAppointmentRepository, patient_repo: IPatientRepository, doctor_repo: IDoctorRepository):
        self._appointment_repo = appointment_repo
        self._patient_repo = patient_repo
        self._doctor_repo = doctor_repo

    def book_appointment(self, appointment: Appointment):
        if not self._patient_repo.find_by_id(appointment.patient_id):
            raise ValueError("Invalid patient ID")
        if not self._doctor_repo.find_by_id(appointment.doctor_id):
            raise ValueError("Invalid doctor ID")
        if self._count_appointments(appointment.patient_id) >= 5:
            raise ValueError("Patient cannot book more than 5 appointments")
        self._appointment_repo.save(appointment)

    def _count_appointments(self, patient_id: str) -> int:
        return len([appt for appt in self._appointment_repo.find_all() if appt.patient_id == patient_id])

    def get_appointment(self, appointment_id: str) -> Appointment:
        appt = self._appointment_repo.find_by_id(appointment_id)
        if not appt:
            raise ValueError("Appointment not found")
        return appt

    def cancel_appointment(self, appointment_id: str):
        if not self._appointment_repo.find_by_id(appointment_id):
            raise ValueError("Cannot cancel non-existent appointment")
        self._appointment_repo.delete(appointment_id)

    def list_appointments(self):
        return self._appointment_repo.find_all()
