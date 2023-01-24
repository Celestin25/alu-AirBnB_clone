#!/usr/bin/python3
"""
    contains unittests for the BaseModel class methods.
"""
import json
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelMethods(unittest.TestCase):
    """Unittest test class for BaseModel class"""

    def setUp(self):
        """Set up classes to be used to run the tests"""
        self.base_1 = BaseModel()
        self.base_2 = BaseModel()

    def tearDown(self):
        """Tear down the resources that had been setup to run tests"""
        del self.base_1
        del self.base_2

    def test_attributes_exist(self):
        """Test that class BaseModel has the required methods and attributes"""
        self.assertTrue(hasattr(BaseModel, '__init__'))
        self.assertTrue(hasattr(self.base_1, 'id'))
        self.assertTrue(hasattr(self.base_1, 'created_at'))
        self.assertTrue(hasattr(self.base_1, 'updated_at'))
        self.assertTrue(hasattr(self.base_1, 'save'))
        self.assertTrue(hasattr(self.base_1, 'to_dict'))
        self.assertTrue(hasattr(BaseModel, '__str__'))

    def test_unique_IDs(self):
        """Test that two instances of BaseModel class are assigned different
            unique IDs
        """
        self.assertNotEqual(self.base_1.id, self.base_2.id)

    def test_kwargs_initialization(self):
        """Test the initialization of a class using kwargs"""
        kwargs = {"__class__": "BaseModel", "created_at":
                  "2021-06-25T19:52:36.252305",
                  "id": "83b3c8a8-b72b-4472-9d80-c52b2e090f04",
                  "updated_at": "2021-06-25T19:52:36.252312"}
        Test_Base = BaseModel(**kwargs)
        self.assertEqual(Test_Base.id, kwargs['id'])
        self.assertEqual(Test_Base.created_at.isoformat(),
                         kwargs['created_at'])
        self.assertEqual(Test_Base.updated_at.isoformat(),
                         kwargs['updated_at'])

    def test_str_representation(self):
        """Test the format of the return value of the __str__ method"""
        msg = "[{}] ({}) {}".format(type(self.base_1).__name__, self.base_1.id,
                                    self.base_1.__dict__)
        self.assertEqual(str(self.base_1), msg)

    def test_to_dict(self):
        """Test the return value of the to_dict() method"""
        test_dict = {key: value for key, value in self.base_1.__dict__.items()}
        test_dict['created_at'] = self.base_1.created_at.isoformat()
        test_dict['updated_at'] = self.base_1.updated_at.isoformat()
        test_dict['__class__'] = type(self.base_1).__name__
        self.assertEqual(self.base_1.to_dict(), test_dict)


class Test_Base_Model_save(unittest.TestCase):
    """Unittest class for testing BaseModel's save method"""

    def setUp(self):
        """Set up resources required to run tests"""
        if os.path.isfile("my_file.json"):
            os.rename("my_file.json", "my_tmp")
        self.base_1 = BaseModel()
        self.base_2 = BaseModel()

    def tearDown(self):
        """Tear down resources used to run tests"""
        if os.path.isfile("my_file.json"):
            os.remove("my_file.json")
        if os.path.isfile("my_tmp"):
            os.rename("my_tmp", "my_file.json")
        del self.base_1
        del self.base_2

    def test_updated_at_save(self):
        """Test updated_at attribute is actually updated"""
        time_1 = self.base_1.updated_at
        sleep(.5)
        self.base_1.save()
        self.assertNotEqual(time_1, self.base_1.updated_at)
        self.assertLess(time_1, self.base_1.updated_at)

    def test_object_saved(self):
        """Test whether an object is stored in a file when using save method"""
        self.base_1.save()
        try:
            with open("my_file.json", mode='r', encoding='UTF-8') as f:
                saved_data = json.load(f)

            base_1_id = "BaseModel." + self.base_1.id
            value = saved_data[base_1_id]
            self.assertEqual(value, self.base_1.to_dict())
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()
