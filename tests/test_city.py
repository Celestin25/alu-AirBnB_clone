#!/usr/bin/python3
"""
 user.py Unittest
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """testing city class instances and methods"""

    c = City()

    def test_class_exists(self):
        """testing if class City exists"""
        self.assertEqual(str(type(self.c)), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        """determining whether city is a BaseModel subclass"""
        self.assertTrue(self.c, City)

    def testHasAttributes(self):
        """checking the existence of class attributes"""
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'name'))
        self.assertTrue(hasattr(self.c, 'id'))
        self.assertTrue(hasattr(self.c, 'created_at'))
        self.assertTrue(hasattr(self.c, 'updated_at'))

    def test_types(self):
        """determines whether the attribute's type is the appropriate one."""
        self.assertIsInstance(self.c.state_id, str)
        self.assertIsInstance(self.c.name, str)
        self.assertIsInstance(self.c.id, str)
        self.assertIsInstance(self.c.created_at, datetime.datetime)
        self.assertIsInstance(self.c.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

