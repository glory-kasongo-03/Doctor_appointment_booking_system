import unittest
from creational_patterns.simple_factory import UserFactory, Patient, Doctor


# The Simple Factory pattern provides a static method to create objects without exposing the instantiation logic to the client. It encapsulates the object creation process and allows for easy addition of new types.

class TestSimpleFactory(unittest.TestCase):
    def test_patient_creation(self):
        patient = UserFactory.create_user("patient")
        self.assertIsInstance(patient, Patient)

    def test_doctor_creation(self):
        doctor = UserFactory.create_user("doctor")
        self.assertIsInstance(doctor, Doctor)

    def test_invalid_user(self):
        with self.assertRaises(ValueError):
            UserFactory.create_user("unknown")
    
