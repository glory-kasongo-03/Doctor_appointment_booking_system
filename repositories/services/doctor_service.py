from repositories.i_doctor_repository import IDoctorRepository
from doctor import Doctor

class DoctorService:
    def __init__(self, repository: IDoctorRepository):
        self._repository = repository

    def register_doctor(self, doctor: Doctor):
        if not doctor.name or not doctor.id:
            raise ValueError("Doctor must have a name and ID")
        self._repository.save(doctor)

    def get_doctor(self, doctor_id: str) -> Doctor:
        doctor = self._repository.find_by_id(doctor_id)
        if not doctor:
            raise ValueError("Doctor not found")
        return doctor

    def list_doctors(self):
        return self._repository.find_all()

    def delete_doctor(self, doctor_id: str):
        if not self._repository.find_by_id(doctor_id):
            raise ValueError("Cannot delete non-existent doctor")
        self._repository.delete(doctor_id)
