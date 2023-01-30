#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        
        self.storage = FileStorage()

    def test_attrs(self):

        self.assertFalse(hasattr(self.storage, "milkyway.json"))

if "__main__" == __name__:
    unittest.main()
