#!/usr/bin/python3
"""
 amenity.py Unittest

"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """testing amenity class instances and methods"""

    m = Amenity()

    def test_class_exists(self):
        """testing if class amenity exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.m)), res)

    def test_user_inheritance(self):
        """determining whether city is a BaseModel subclass"""
        self.assertIsInstance(self.m, Amenity)

    def testHasAttributes(self):
        """
        checking the existence of class attributes

        """
        self.assertTrue(hasattr(self.m, 'name'))
        self.assertTrue(hasattr(self.m, 'id'))
        self.assertTrue(hasattr(self.m, 'created_at'))
        self.assertTrue(hasattr(self.m, 'updated_at'))

    def test_types(self):

        """
        determines whether the attribute's type is the appropriate one.

        """

        self.assertIsInstance(self.m.name, str)
        self.assertIsInstance(self.m.id, str)
        self.assertIsInstance(self.m.created_at, datetime.datetime)
        self.assertIsInstance(self.m.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

