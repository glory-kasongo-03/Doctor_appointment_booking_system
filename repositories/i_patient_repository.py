from typing import List
from .repository_interface_design import IRepository
from patient import Patient

class IPatientRepository(IRepository[Patient, int]):
    def find_by_email(self, email: str) -> Patient:
        pass
