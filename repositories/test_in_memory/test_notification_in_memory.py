import unittest
from repositories.in_memory.notification_in_memory import InMemoryNotificationRepository
from notification import Notification

class TestInMemoryNotificationRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryNotificationRepository()
        self.notification = Notification(id="n1", message="Test Message")

    def test_save_and_find_by_id(self):
        self.repo.save(self.notification)
        self.assertEqual(self.repo.find_by_id("n1"), self.notification)

    def test_find_all(self):
        self.repo.save(self.notification)
        self.assertIn(self.notification, self.repo.find_all())

    def test_delete(self):
        self.repo.save(self.notification)
        self.repo.delete("n1")
        self.assertIsNone(self.repo.find_by_id("n1"))
