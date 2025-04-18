from typing import List
from user_account import UserAccount
from appointment import Appointment
from ehr import EHR

class Patient(UserAccount):
    def __init__(self, user_id: str, username: str, password: str, name: str, email: str, phone: str, insurance_info: str):
        super().__init__(user_id, username, password, role="Patient")
        self._patient_id = user_id
        self._name = name
        self._email = email
        self._phone = phone
        self._insurance_info = insurance_info
        self.appointments: List[Appointment] = []
        self.ehrs: List[EHR] = []

    def register(self):
        print(f"Patient {self._name} registered.")

    def book_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)
        print(f"Appointment booked for {self._name}.")

    def cancel_appointment(self, appointment_id: str):
        self.appointments = [appt for appt in self.appointments if appt.appointment_id != appointment_id]
        print(f"Appointment {appointment_id} cancelled for {self._name}.")
