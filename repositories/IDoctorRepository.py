from typing import List
from Repository_Interface_Design import IRepository
from doctor import Doctor

class IDoctorRepository(IRepository[Doctor, int]):
    def find_by_specialization(self, specialization: str) -> List[Doctor]:
        pass
