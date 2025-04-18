import unittest
from creational_patterns.singleton import DatabaseConnection
# The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.

class TestSingletonPattern(unittest.TestCase):
    def test_singleton_instance(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        self.assertIs(db1, db2)  # Both should refer to the same instance
