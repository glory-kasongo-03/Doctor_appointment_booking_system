# repository_in_memory/in_memory_appointment_repo.py
from typing import List
from appointment import Appointment
from IAppointmentRepository import IAppointmentRepository

class InMemoryAppointmentRepository(IAppointmentRepository):
    def __init__(self):
        self._storage = {}

    def get_all(self) -> List[Appointment]:
        return list(self._storage.values())

    def get_by_id(self, entity_id: int) -> Appointment:
        return self._storage.get(entity_id)

    def add(self, entity: Appointment) -> None:
        self._storage[entity.id] = entity

    def update(self, entity: Appointment) -> None:
        self._storage[entity.id] = entity

    def delete(self, entity_id: int) -> None:
        if entity_id in self._storage:
            del self._storage[entity_id]

    def find_by_patient_id(self, patient_id: int) -> List[Appointment]:
        return [a for a in self._storage.values() if a.patient_id == patient_id]

    def find_by_doctor_id(self, doctor_id: int) -> List[Appointment]:
        return [a for a in self._storage.values() if a.doctor_id == doctor_id]
