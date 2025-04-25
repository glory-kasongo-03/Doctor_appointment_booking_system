import unittest
from repositories.in_memory.doctor_in_memory import InMemoryDoctorRepository
from doctor import Doctor

class TestInMemoryDoctorRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryDoctorRepository()
        self.doctor = Doctor(id="d1", name="Dr. Smith")

    def test_save_and_find_by_id(self):
        self.repo.save(self.doctor)
        self.assertEqual(self.repo.find_by_id("d1"), self.doctor)

    def test_find_all(self):
        self.repo.save(self.doctor)
        self.assertIn(self.doctor, self.repo.find_all())

    def test_delete(self):
        self.repo.save(self.doctor)
        self.repo.delete("d1")
        self.assertIsNone(self.repo.find_by_id("d1"))
