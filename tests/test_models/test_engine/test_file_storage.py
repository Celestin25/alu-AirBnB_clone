import os
import json
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestStorage(unittest.TestCase):
    """Test cases for FileStorage class."""
    file_location = 'file.json'

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_location):
            os.remove(self.file_location)
        del self.storage

    def test_if_instance(self):
        """Test if storage is an instance of FileStorage"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_class_type(self):
        """Test if storage is of class FileStorage"""
        self.assertEqual(str(type(self.storage)), "<class 'models.engine.file_storage.FileStorage'>")

    def test_file_creation(self):
        """Test if file.json is created after calling save method"""
        self.assertFalse(os.path.exists(self.file_location))
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_location))

    def test_add_object(self):
        """Test if object is added to storage"""
        self.assertEqual(self.storage.all(), {})
        base = BaseModel()
        self.storage.new(base)
        self.assertIn(base, self.storage.all().values())

    def test_type_of_all(self):
        """Test if all method returns a dictionary"""
        self.assertEqual(type(self.storage.all()), dict)

    def test_reload_method(self):
        """Test if reload method returns a dictionary"""
        self.storage.reload()
        self.assertIsInstance(self.storage.all(), type({}))

    def test_clear_and_reload(self):
        """Test if reload method returns an empty dictionary after clearing all method"""
        storage = FileStorage()
        storage.all().clear()
        storage.reload()
        self.assertEqual({}, self.storage.all())
        del storage

class TestStorageReload(unittest.TestCase):
    """Test reload method again"""
    file_location = 'file.json'

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_location):
            os.remove(self.file_location)
        del self.storage

    def test_reload_with_object(self):
        """Test reload method with object saved"""
        base = BaseModel()
        base.save()

        self.storage.reload()

        object_key = "{}.{}".format(base.__class__.__name__, base.id)
        self.assertIn(object_key, self.storage.all())

        self.assertEqual(self.storage.all()[object_key].id, base.id)

if __name__ ==
