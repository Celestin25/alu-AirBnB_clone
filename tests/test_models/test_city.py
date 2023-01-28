#!/usr/bin/python3

"""Unit test for City class."""

import unittest

from models.city import City

from models.base_model import BaseModel

class VerifyCity(unittest.TestCase):
"""Test cases for City class."""
def test_is_instance(self):
    """Check if the city is an instance of City."""
    city = City()
    self.assertIsInstance(city, City)

def test_type(self):
    """Verify that city is of the correct class type."""
    city = City()
    self.assertEqual(str(type(city)), "<class 'models.city.City'>")

def test_is_subclass(self):
    """Check if the city is a subclass of BaseModel."""
    city = City()
    self.assertTrue(issubclass(type(city), BaseModel))

def test_name_attribute(self):
    """Check if the city's name attribute is empty string."""
    city = City()
    self.assertEqual(city.name, "")

def test_state_id_attribute(self):
    """Check if the city's state_id attribute is empty string."""
    city = City()
    self.assertEqual(city.state_id, "")
    if name == "main":
unittest.main()
