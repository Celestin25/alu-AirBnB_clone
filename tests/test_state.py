#!/usr/bin/python3
"""
state.py Unittest
"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ testing state class instances and methods"""

    s = State()

    def test_class_exists(self):
        """testing if class state exists"""
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.s)), res)

    def test_user_inheritance(self):
        """determining whether state is a BaseModel subclass"""
        self.assertIsInstance(self.s, State)

    def testHasAttributes(self):
        """checking the existence of class attributes"""
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))

    def test_types(self):
        """determines whether the attribute's type is the appropriate one."""
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime.datetime)
        self.assertIsInstance(self.s.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

