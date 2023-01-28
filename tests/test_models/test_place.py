#!/usr/bin/python3

"""Unit tests for Place class"""

import unittest

from place_model import Place
from city_model import City
from user_model import User

from base_model import BaseModel


class TestPlaceMethods(unittest.TestCase):
    """Test cases for Place class"""

    def test_place_instance(self):
        """Test creating an instance of Place"""
        test_place = Place()
        self.assertIsInstance(test_place, Place)

    def test_place_class(self):
        """Test if the instance is of the Place class"""
        test_place = Place()
        self.assertEqual(str(type(test_place)), "<class 'place_model.Place'>")

    def test_place_subclass(self):
        """Test if Place is a subclass of BaseModel"""
        test_place = Place()
        self.assertTrue(issubclass(type(test_place), BaseModel))

    def test_place_attributes(self):
        """Test place attributes"""
        test_city = City()
        test_user = User()
        test_place = Place()
        test_place.user_id = test_user.id
        test_place.city_id = test_city.id
        self.assertIsNotNone(test_place.id)
        self.assertEqual(test_place.user_id, test_user.id)
        self.assertEqual(test_place.city_id, test_city.id)
        self.assertEqual(test_place.name, "")
        self.assertEqual(test_place.description, "")
        self.assertEqual(test_place.number_rooms, 0)
        self.assertEqual(test_place.number_bathrooms, 0)
        self.assertEqual(test_place.max_guest, 0)
        self.assertEqual(test_place.price_by_night, 0)
        self.assertEqual(test_place.latitude, 0)
        self.assertEqual(test_place.longitude, 0)
        self.assertEqual(test_place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
