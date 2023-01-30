#!/usr/bin/python3
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):

    def setUp(self):
    
        self.test_model1 = Review()
        self.test_model2 = Review()

    def test_basic_setup(self):
    
        self.assertTrue(hasattr(self.test_model1, "place_id"))
        self.assertTrue(hasattr(self.test_model1, "user_id"))
        self.assertTrue(hasattr(self.test_model1, "text"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.place_id
        m2c = self.test_model2.place_id
        self.assertTrue(m1c == m2c)
        self.assertTrue(type(m1c) is str)

    def test_types(self):
    
        self.assertTrue(type(self.test_model1.place_id) is str)
        self.assertTrue(type(self.test_model1.user_id) is str)
        self.assertTrue(type(self.test_model1.text) is str)

    def test_save(self):
    
        m1u = self.test_model1.updated_at
        self.test_model1.save()
        m1u_saved = self.test_model1.updated_at
        self.assertFalse(m1u == m1u_saved)

if __name__ == '__main__':
    unittest.main()
