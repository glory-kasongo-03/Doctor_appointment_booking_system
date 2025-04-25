from typing import List
from repository_interface_design import IRepository
from appointment import Appointment

class IAppointmentRepository(IRepository[Appointment, int]):
    def find_by_patient_id(self, patient_id: int) -> List[Appointment]:
        pass

    def find_by_doctor_id(self, doctor_id: int) -> List[Appointment]:
        pass
