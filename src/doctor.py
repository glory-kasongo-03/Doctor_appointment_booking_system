from typing import List
from user_account import UserAccount
from appointment import Appointment
from ehr import EHR

class Doctor(UserAccount):
    def __init__(self, user_id: str, username: str, password: str, name: str, specialization: str, license_number: str, availability: str):
        super().__init__(user_id, username, password, role="Doctor")
        self._doctor_id = user_id
        self._name = name
        self._specialization = specialization
        self._license_number = license_number
        self._availability = availability
        self.appointments: List[Appointment] = []
        self.ehrs: List[EHR] = []

    def approve_appointment(self, appointment: Appointment):
        appointment.status = "Approved"
        print(f"Appointment {appointment.appointment_id} approved by Dr. {self._name}")

    def update_ehr(self, ehr: EHR, new_diagnosis: str, new_treatment_plan: str):
        ehr.diagnosis = new_diagnosis
        ehr.treatment_plan = new_treatment_plan
        print(f"EHR {ehr.ehr_id} updated by Dr. {self._name}")
