# repository_in_memory/in_memory_doctor_repository.py
from repositories.i_doctor_repository import IDoctorRepository
from doctor import Doctor
from typing import Dict, List

class InMemoryDoctorRepository(IDoctorRepository):
    def __init__(self):
        self._storage: Dict[int, Doctor] = {}

    def get_all(self) -> List[Doctor]:
        return list(self._storage.values())

    def get_by_id(self, doctor_id: int) -> Doctor:
        return self._storage.get(doctor_id)

    def add(self, doctor: Doctor) -> None:
        self._storage[doctor.id] = doctor

    def update(self, doctor: Doctor) -> None:
        if doctor.id in self._storage:
            self._storage[doctor.id] = doctor

    def delete(self, doctor_id: int) -> None:
        self._storage.pop(doctor_id, None)
