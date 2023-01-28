#!/usr/bin/python3

"""Unittest for Amenity Class."""

import unittest

from models.amenity import Amenity

from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
"""Test cases for Amenity class."""
def test_instance(self):
    """test instance."""
    test_amenity = Amenity()
    self.assertIsInstance(test_amenity, Amenity)

def test_is_class(self):
    """test instance."""
    test_amenity = Amenity()
    self.assertEqual(str(type(test_amenity)),
                     "<class 'models.amenity.Amenity'>")

def test_is_subclass(self):
    """test is_subclass."""
    test_amenity = Amenity()
    self.assertTrue(issubclass(type(test_amenity), BaseModel))

def test_attr(self):
    """test is_subclass."""
    test_amenity = Amenity()
    self.assertEqual(test_amenity.name, "")
    self.assertIsNotNone(test_amenity.id)
    if name == "main":
unittest.main()
