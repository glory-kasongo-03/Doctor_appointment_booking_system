import unittest
from repositories.in_memory.appointment_in_memory import InMemoryAppointmentRepository
from appointment import Appointment

class TestInMemoryAppointmentRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryAppointmentRepository()
        self.appointment = Appointment(id="a1", patient_id="p1", doctor_id="d1")

    def test_save_and_find_by_id(self):
        self.repo.save(self.appointment)
        self.assertEqual(self.repo.find_by_id("a1"), self.appointment)

    def test_find_all(self):
        self.repo.save(self.appointment)
        self.assertIn(self.appointment, self.repo.find_all())

    def test_delete(self):
        self.repo.save(self.appointment)
        self.repo.delete("a1")
        self.assertIsNone(self.repo.find_by_id("a1"))
