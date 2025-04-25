from typing import List
from Repository_Interface_Design import IRepository
from patient import Patient

class IPatientRepository(IRepository[Patient, int]):
    def find_by_email(self, email: str) -> Patient:
        pass
