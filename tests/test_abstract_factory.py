import unittest
from creational_patterns.abstract_factory import (
    WebUIFactory,
    MobileUIFactory,
)

# The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. 
# It allows for the creation of objects that belong to a specific family, ensuring that they are compatible with each other.

class TestAbstractFactory(unittest.TestCase):
    def test_web_ui(self):
        factory = WebUIFactory()
        button = factory.create_button()
        self.assertEqual(button.render(), "Rendered Web Button")

    def test_mobile_ui(self):
        factory = MobileUIFactory()
        button = factory.create_button()
        self.assertEqual(button.render(), "Rendered Mobile Button")
