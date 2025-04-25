from typing import List
from repository_interface_design import IRepository
from doctor import Doctor

class IDoctorRepository(IRepository[Doctor, int]):
    def find_by_specialization(self, specialization: str) -> List[Doctor]:
        pass
