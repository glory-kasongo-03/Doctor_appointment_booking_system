class Appointment:
    def __init__(self):
        self.date = None
        self.time = None
        self.doctor = None
        self.patient = None
        self.notes = ""

class AppointmentBuilder:
    def __init__(self):
        self.appointment = Appointment()

    def set_date(self, date):
        self.appointment.date = date
        return self

    def set_time(self, time):
        self.appointment.time = time
        return self

    def set_doctor(self, doctor):
        self.appointment.doctor = doctor
        return self

    def set_patient(self, patient):
        self.appointment.patient = patient
        return self

    def add_notes(self, notes):
        self.appointment.notes = notes
        return self

    def build(self):
        return self.appointment
