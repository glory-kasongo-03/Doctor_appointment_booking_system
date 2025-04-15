from datetime import datetime

class UserAccount:
    def __init__(self, user_id: str, username: str, password: str, role: str):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._role = role

    def login(self):
        print(f"{self._username} logged in.")

    def logout(self):
        print(f"{self._username} logged out.")

    def change_password(self, new_password: str):
        self._password = new_password
        print("Password changed successfully.")

class Patient(UserAccount):
    def __init__(self, user_id: str, username: str, password: str, email: str, phone: str, insurance_info: str):
        super().__init__(user_id, username, password, role="Patient")
        self._email = email
        self._phone = phone
        self._insurance_info = insurance_info
        self.appointments = []
        self.ehr_records = []

    def register(self):
        print(f"Patient {self._username} registered.")

    def book_appointment(self, appointment):
        self.appointments.append(appointment)
        print(f"Appointment booked for {self._username}.")

    def cancel_appointment(self, appointment):
        if appointment in self.appointments:
            self.appointments.remove(appointment)
            print("Appointment canceled.")

class Doctor(UserAccount):
    def __init__(self, user_id: str, username: str, password: str, specialization: str, license_number: str, availability: str):
        super().__init__(user_id, username, password, role="Doctor")
        self._specialization = specialization
        self._license_number = license_number
        self._availability = availability
        self.ehr_records = []

    def approve_appointment(self, appointment):
        appointment.status = "Approved"
        print(f"Appointment {appointment._appointment_id} approved.")

    def update_ehr(self, ehr):
        print(f"EHR {ehr._ehr_id} updated.")

class Appointment:
    def __init__(self, appointment_id: str, date_time: datetime, status: str, type_: str):
        self._appointment_id = appointment_id
        self._date_time = date_time
        self._status = status
        self._type = type_

    def confirm(self):
        self._status = "Confirmed"
        print("Appointment confirmed.")

    def reschedule(self, new_date_time: datetime):
        self._date_time = new_date_time
        print("Appointment rescheduled.")

    def cancel(self):
        self._status = "Canceled"
        print("Appointment canceled.")

class EHR:
    def __init__(self, ehr_id: str, medical_history: str, diagnosis: str, treatment_plan: str):
        self._ehr_id = ehr_id
        self._medical_history = medical_history
        self._diagnosis = diagnosis
        self._treatment_plan = treatment_plan

    def view_record(self):
        return vars(self)

    def update_record(self, new_diagnosis: str, new_treatment_plan: str):
        self._diagnosis = new_diagnosis
        self._treatment_plan = new_treatment_plan
        print("EHR updated.")

class Notification:
    def __init__(self, notification_id: str, message: str, status: str, timestamp: datetime):
        self._notification_id = notification_id
        self._message = message
        self._status = status
        self._timestamp = timestamp

    def send(self):
        print(f"Notification sent: {self._message}")

    def mark_as_read(self):
        self._status = "Read"
        print("Notification marked as read.")

class SystemReport:
    def __init__(self, report_id: str, type_: str, content: str):
        self._report_id = report_id
        self._type = type_
        self._content = content

    def generate(self):
        print(f"Generating report {self._report_id}")

    def export(self):
        print("Report exported.")

