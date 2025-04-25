import unittest
from repositories.repository_interface_design import Patient
from repositories.in_memory.in_memory_repository import InMemoryRepository

class TestInMemoryRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryRepository[Patient, int]()
        self.patient = Patient(id=1, name="John Doe", email="john@example.com")
        self.repo.add(self.patient)

    def test_get_all(self):
        all_patients = self.repo.get_all()
        self.assertEqual(len(all_patients), 1)
        self.assertEqual(all_patients[0].name, "John Doe")

    def test_get_by_id(self):
        patient = self.repo.get_by_id(1)
        self.assertIsNotNone(patient)
        self.assertEqual(patient.email, "john@example.com")

    def test_update(self):
        updated = Patient(id=1, name="John Smith", email="johnsmith@example.com")
        self.repo.update(updated)
        result = self.repo.get_by_id(1)
        self.assertEqual(result.name, "John Smith")

    def test_delete(self):
        self.repo.delete(1)
        self.assertIsNone(self.repo.get_by_id(1))

    def test_add_multiple(self):
        self.repo.add(Patient(id=2, name="Jane Roe", email="jane@example.com"))
        self.repo.add(Patient(id=3, name="Alice Smith", email="alice@example.com"))
        self.assertEqual(len(self.repo.get_all()), 3)

if __name__ == '__main__':
    unittest.main()