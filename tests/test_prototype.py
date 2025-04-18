import unittest
from creational_patterns.prototype import Report
# The Prototype pattern allows for creating new objects by copying an existing object, known as the prototype.

class TestPrototypePattern(unittest.TestCase):
    def test_clone(self):
        original = Report("Monthly Report", "Details of the month")
        cloned = original.clone()
        self.assertNotEqual(id(original), id(cloned))  # Ensure a new object is created
        self.assertEqual(original.title, cloned.title)
        self.assertEqual(original.content, cloned.content)
