import unittest
from repositories.in_memory.admin_in_memory import InMemoryAdminRepository
from user_account import Admin

class TestInMemoryAdminRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryAdminRepository()
        self.admin = Admin(id="a1", username="admin1")

    def test_save_and_find_by_id(self):
        self.repo.save(self.admin)
        self.assertEqual(self.repo.find_by_id("a1"), self.admin)

    def test_find_all(self):
        self.repo.save(self.admin)
        self.assertIn(self.admin, self.repo.find_all())

    def test_delete(self):
        self.repo.save(self.admin)
        self.repo.delete("a1")
        self.assertIsNone(self.repo.find_by_id("a1"))
