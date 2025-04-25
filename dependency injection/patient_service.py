# services/patient_service.py
from typing import List
from patient import Patient
from repositories.Repository_Interface_Design import IRepository

class PatientService:
    def __init__(self, repository: IRepository[Patient, int]):
        self._repository = repository

    def get_all_patients(self) -> List[Patient]:
        return self._repository.get_all()

    def register_patient(self, patient: Patient) -> None:
        self._repository.add(patient)

    def update_patient(self, patient: Patient) -> None:
        self._repository.update(patient)

    def delete_patient(self, patient_id: int) -> None:
        self._repository.delete(patient_id)
