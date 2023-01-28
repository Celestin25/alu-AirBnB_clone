import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def test_instance(self):
        """Test that user is an instance of User."""
        user = User()
        self.assertIsInstance(user, User)

    def test_class(self):
        """Test that the user is of class User."""
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")

    def test_subclass(self):
        """Test that user is a subclass of BaseModel."""
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_has_id(self):
        """Test that the user has an id"""
        user = User()
        self.assertIsNotNone(user.id)

    def test_email(self):
        """Test that the user email can be set and retrieved."""
        user = User()
        self.assertEqual(user.email, "")
        user.email = "airbnb@mail.com"
        self.assertEqual(user.email, "airbnb@mail.com")

    def test_password(self):
        """Test that the user password can be set and retrieved."""
        user = User()
        self.assertEqual(user.password, "")
        user.password = "root"
        self.assertEqual(user.password, "root")

    def test_first_name(self):
        """Test that the user first name can be set and retrieved."""
        user = User()
        self.assertEqual(user.first_name, "")
        user.first_name = "Betty"
        self.assertEqual(user.first_name, "Betty")

    def test_last_name(self):
        """Test that the user last name can be set and retrieved."""
        user = User()
        self.assertEqual(user.last_name, "")
        user.last_name = "Bar"
        self.assertEqual(user.last_name, "Bar")

if __name__ == '__main__':
    unittest.main()
