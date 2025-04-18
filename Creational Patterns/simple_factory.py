class User:
    def login(self):
        pass

class Patient(User):
    def book_appointment(self):
        print("Patient booked an appointment.")

class Doctor(User):
    def approve_appointment(self):
        print("Doctor approved the appointment.")

class Admin(User):
    def generate_report(self):
        print("Admin generated a report.")

class UserFactory:
    @staticmethod
    def create_user(user_type):
        if user_type == "patient":
            return Patient()
        elif user_type == "doctor":
            return Doctor()
        elif user_type == "admin":
            return Admin()
        else:
            raise ValueError("Unknown user type")
