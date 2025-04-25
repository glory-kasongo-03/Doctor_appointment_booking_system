# repository_in_memory/in_memory_patient_repository.py
from IPatientRepository import IPatientRepository
from patient import Patient
from typing import Dict, Optional, List

class InMemoryPatientRepository(IPatientRepository):
    def __init__(self):
        self._storage: Dict[int, Patient] = {}

    def save(self, entity: Patient) -> None:
        self._storage[entity.id] = entity  # Create or Update

    def find_by_id(self, id: int) -> Optional[Patient]:
        return self._storage.get(id)

    def find_all(self) -> List[Patient]:
        return list(self._storage.values())

    def delete(self, id: int) -> None:
        self._storage.pop(id, None)
