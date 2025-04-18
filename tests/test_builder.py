import unittest
from creational_patterns.builder import AppointmentBuilder
# The Builder pattern is used to construct a complex object step by step. 
# It allows for the creation of different representations of an object using the same construction process.

class TestBuilderPattern(unittest.TestCase):
    def test_appointment_build(self):
        builder = AppointmentBuilder()
        appointment = (builder.set_date("2025-04-18")
                              .set_time("10:00 AM")
                              .set_doctor("Dr. Smith")
                              .set_patient("John Doe")
                              .add_notes("First appointment")
                              .build())
        self.assertEqual(appointment.date, "2025-04-18")
        self.assertEqual(appointment.time, "10:00 AM")
        self.assertEqual(appointment.doctor, "Dr. Smith")
        self.assertEqual(appointment.patient, "John Doe")
        self.assertEqual(appointment.notes, "First appointment")
