#!/usr/bin/python3

"""Unit testing for the Review class."""

import unittest

from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
"""Test cases for the Review class."""
def test_instance_creation(self):
    """Tests if an instance of the class can be created."""
    review = Review()
    self.assertIsInstance(review, Review)

def test_class_type(self):
    """Tests if the object created is of the correct class type."""
    review = Review()
    self.assertEqual(str(type(review)), "<class 'models.review.Review'>")

def test_inheritance(self):
    """Tests if the class inherits from the BaseModel class."""
    review = Review()
    self.assertTrue(issubclass(type(review), BaseModel))

def test_attributes(self):
    """Tests if the class has the correct attributes."""
    review = Review()
    self.assertIsNotNone(review.id)
    self.assertEqual(review.text, "")
    self.assertEqual(review.user_id, "")
    self.assertEqual(review.place_id, "")
    if name == "main":
unittest.main()
