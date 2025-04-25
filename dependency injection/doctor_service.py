# services/doctor_service.py
from repositories.i_doctor_repository import IDoctorRepository
from doctor import Doctor
from typing import List

class DoctorService:
    def __init__(self, repository: IDoctorRepository):
        self._repository = repository

    def add_doctor(self, doctor: Doctor) -> None:
        self._repository.add(doctor)

    def get_all_doctors(self) -> List[Doctor]:
        return self._repository.get_all()

    def update_doctor(self, doctor: Doctor) -> None:
        self._repository.update(doctor)

    def delete_doctor(self, doctor_id: int) -> None:
        self._repository.delete(doctor_id)
