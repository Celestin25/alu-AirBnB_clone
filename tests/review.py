#!/usr/bin/python3
"""
review.py Unittest
"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """testing review class instances and methods"""

    R = Review()

    def test_class_exists(self):
        """testing if class review exists"""
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.R)), res)

    def test_user_inheritance(self):
        """determining whether review is a BaseModel subclass"""
        self.assertIsInstance(self.R, Review)

    def testHasAttributes(self):
        """checking the existence of class attributes"""
        self.assertTrue(hasattr(self.R, 'place_id'))
        self.assertTrue(hasattr(self.R, 'user_id'))
        self.assertTrue(hasattr(self.R, 'text'))
        self.assertTrue(hasattr(self.R, 'id'))
        self.assertTrue(hasattr(self.R, 'created_at'))
        self.assertTrue(hasattr(self.R, 'updated_at'))

    def test_types(self):
        """determines whether the attribute's type is the appropriate one."""
        self.assertIsInstance(self.R.place_id, str)
        self.assertIsInstance(self.R.user_id, str)
        self.assertIsInstance(self.R.text, str)
        self.assertIsInstance(self.R.id, str)
        self.assertIsInstance(self.R.created_at, datetime.datetime)
        self.assertIsInstance(self.R.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

