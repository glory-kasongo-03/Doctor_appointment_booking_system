from datetime import datetime
from typing import List
from notification import Notification

class Appointment:
    def __init__(self, appointment_id: str, date_time: datetime, status: str, type_: str):
        self.appointment_id = appointment_id
        self.date_time = date_time
        self.status = status
        self.type = type_
        self.notifications: List[Notification] = []

    def confirm(self):
        self.status = "Confirmed"
        print(f"Appointment {self.appointment_id} confirmed.")

    def reschedule(self, new_datetime: datetime):
        self.date_time = new_datetime
        print(f"Appointment {self.appointment_id} rescheduled.")

    def cancel(self):
        self.status = "Cancelled"
        print(f"Appointment {self.appointment_id} cancelled.")
