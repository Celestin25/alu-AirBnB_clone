#!/usr/bin/python3

"""Unit testing for the State class."""

import unittest

from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
"""Test cases for the State class."""
def test_instance_creation(self):
    """Tests if an instance of the class can be created."""
    state = State()
    self.assertIsInstance(state, State)

def test_class_type(self):
    """Tests if the object created is of the correct class type."""
    state = State()
    self.assertEqual(str(type(state)), "<class 'models.state.State'>")

def test_inheritance(self):
    """Tests if the class inherits from the BaseModel class."""
    state = State()
    self.assertTrue(issubclass(type(state), BaseModel))

def test_attributes(self):
    """Tests if the class has the correct attributes."""
    state = State()
    self.assertIsNotNone(state.id)
    self.assertEqual(state.name, "")
    if name == "main":
unittest.main()
