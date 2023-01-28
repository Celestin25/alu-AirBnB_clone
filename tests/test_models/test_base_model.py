import json
import os
import unittest
import time
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from io import StringIO
from unittest.mock import patch

class TestBaseModelMethods(unittest.TestCase):
    def setUp(self):
        self.test_model = BaseModel()
    
    def test_instance(self):
        self.assertIsInstance(self.test_model, BaseModel)

    def test_class(self):
        self.assertEqual(str(type(self.test_model)), "<class 'models.base_model.BaseModel'>")

    def test_save(self):
        original_time = self.test_model.updated_at
        time.sleep(1)
        self.test_model.save()
        self.assertNotEqual(original_time, self.test_model.updated_at)
        self.assertTrue(self.test_model.updated_at > original_time)

    def test_save_file(self):
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.test_model.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", 'r') as file:
            serialized_content = json.load(file)
            for item in serialized_content.values():
                self.assertIsNotNone(item['__class__'])

    def test_string_representation(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(self.test_model)
            self.assertEqual(fake_out.getvalue(),
                             "[{}] ({}) {}\n".format(self.test_model.__class__.__name__,
                                                     self.test_model.id,
                                                     self.test_model.__dict__))

    def test_to_dict(self):
        dict_representation = self.test_model.to_dict()
        self.assertTrue(dict_representation['__class__'] == self.test_model.__class__.__name__)

if __name__ == "__main__":
    unittest.main()
