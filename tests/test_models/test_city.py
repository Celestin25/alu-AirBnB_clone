#!/usr/bin/python3
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):

    def setUp(self):
        self.test_model1 = City()
        self.test_model2 = City()

    def test_basic_setup(self):
    
        self.assertTrue(hasattr(self.test_model1, "state_id"))
        self.assertTrue(hasattr(self.test_model1, "name"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)

    def test_types(self):
    
        self.assertTrue(type(self.test_model1.state_id) is str)
        self.assertTrue(type(self.test_model1.name) is str)

    def test_save(self):
    
        m1u = self.test_model1.updated_at
        self.test_model1.save()
        m1u_saved = self.test_model1.updated_at
        self.assertFalse(m1u == m1u_saved)

if __name__ == '__main__':
    unittest.main()
