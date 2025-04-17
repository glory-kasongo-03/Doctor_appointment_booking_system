from datetime import datetime
from typing import List, Optional


# Base Class
class UserAccount:
    def __init__(self, user_id: str, username: str, password: str, role: str):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._role = role
        self.notifications: List['Notification'] = []

    def login(self):
        print(f"{self._username} logged in.")

    def logout(self):
        print(f"{self._username} logged out.")

    def change_password(self, new_password: str):
        self._password = new_password
        print(f"Password changed for user {self._username}")

    # Optional: Getter and Setter
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value


class Patient(UserAccount):
    def __init__(self, user_id: str, username: str, password: str, name: str, email: str, phone: str, insurance_info: str):
        super().__init__(user_id, username, password, role="Patient")
        self._patient_id = user_id
        self._name = name
        self._email = email
        self._phone = phone
        self._insurance_info = insurance_info
        self.appointments: List['Appointment'] = []
        self.ehrs: List['EHR'] = []

    def register(self):
        print(f"Patient {self._name} registered.")

    def book_appointment(self, appointment: 'Appointment'):
        self.appointments.append(appointment)
        print(f"Appointment booked for {self._name}.")

    def cancel_appointment(self, appointment_id: str):
        self.appointments = [appt for appt in self.appointments if appt.appointment_id != appointment_id]
        print(f"Appointment {appointment_id} cancelled for {self._name}.")


class Doctor(UserAccount):
    def __init__(self, user_id: str, username: str, password: str, name: str, specialization: str, license_number: str, availability: str):
        super().__init__(user_id, username, password, role="Doctor")
        self._doctor_id = user_id
        self._name = name
        self._specialization = specialization
        self._license_number = license_number
        self._availability = availability
        self.appointments: List['Appointment'] = []
        self.ehrs: List['EHR'] = []

    def approve_appointment(self, appointment: 'Appointment'):
        appointment.status = "Approved"
        print(f"Appointment {appointment.appointment_id} approved by Dr. {self._name}")

    def update_ehr(self, ehr: 'EHR', new_diagnosis: str, new_treatment_plan: str):
        ehr.diagnosis = new_diagnosis
        ehr.treatment_plan = new_treatment_plan
        print(f"EHR {ehr.ehr_id} updated by Dr. {self._name}")


class Appointment:
    def __init__(self, appointment_id: str, date_time: datetime, status: str, type_: str):
        self.appointment_id = appointment_id
        self.date_time = date_time
        self.status = status
        self.type = type_
        self.notifications: List['Notification'] = []

    def confirm(self):
        self.status = "Confirmed"
        print(f"Appointment {self.appointment_id} confirmed.")

    def reschedule(self, new_datetime: datetime):
        self.date_time = new_datetime
        print(f"Appointment {self.appointment_id} rescheduled.")

    def cancel(self):
        self.status = "Cancelled"
        print(f"Appointment {self.appointment_id} cancelled.")


class EHR:
    def __init__(self, ehr_id: str, medical_history: str, diagnosis: str, treatment_plan: str):
        self.ehr_id = ehr_id
        self.medical_history = medical_history
        self.diagnosis = diagnosis
        self.treatment_plan = treatment_plan

    def view_record(self):
        print(f"Viewing EHR {self.ehr_id}")
        return {
            "Medical History": self.medical_history,
            "Diagnosis": self.diagnosis,
            "Treatment Plan": self.treatment_plan
        }

    def update_record(self, new_diagnosis: str, new_treatment_plan: str):
        self.diagnosis = new_diagnosis
        self.treatment_plan = new_treatment_plan
        print(f"EHR {self.ehr_id} updated.")


class Notification:
    def __init__(self, notification_id: str, message: str, status: str, timestamp: datetime):
        self.notification_id = notification_id
        self.message = message
        self.status = status
        self.timestamp = timestamp

    def send(self):
        print(f"Notification {self.notification_id} sent: {self.message}")

    def mark_as_read(self):
        self.status = "Read"
        print(f"Notification {self.notification_id} marked as read.")


class SystemReport:
    def __init__(self, report_id: str, type_: str, content: str, generated_by: UserAccount):
        self.report_id = report_id
        self.type = type_
        self.content = content
        self.generated_by = generated_by

    def generate(self):
        print(f"Report {self.report_id} of type {self.type} generated.")

    def export(self):
        print(f"Report {self.report_id} exported.")
