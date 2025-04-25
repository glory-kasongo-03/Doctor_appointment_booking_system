from typing import List
from Repository_Interface_Design import IRepository
from appointment import Appointment

class IAppointmentRepository(IRepository[Appointment, int]):
    def find_by_patient_id(self, patient_id: int) -> List[Appointment]:
        pass

    def find_by_doctor_id(self, doctor_id: int) -> List[Appointment]:
        pass
