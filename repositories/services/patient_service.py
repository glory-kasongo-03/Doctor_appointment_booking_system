from repositories.i_patient_repository import IPatientRepository
from patient import Patient

class PatientService:
    def __init__(self, repository: IPatientRepository):
        self._repository = repository

    def register_patient(self, patient: Patient):
        if not patient.name or not patient.id:
            raise ValueError("Patient must have a name and ID")
        self._repository.save(patient)

    def get_patient(self, patient_id: str) -> Patient:
        patient = self._repository.find_by_id(patient_id)
        if not patient:
            raise ValueError("Patient not found")
        return patient

    def list_patients(self):
        return self._repository.find_all()

    def delete_patient(self, patient_id: str):
        if not self._repository.find_by_id(patient_id):
            raise ValueError("Cannot delete non-existent patient")
        self._repository.delete(patient_id)
