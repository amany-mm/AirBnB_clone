#!/usr/bin/python3
""" User model tests module. """
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ User model tests """

    def test_parent_model(self):
        """ test inherits from BaseModel """
        self.assertTrue(issubclass(User, BaseModel))

    def test_types(self):
        """ test types """
        user = User()
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)

    def test_attrs(self):
        """ test attrs """
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))

    def test_values(self):
        """ test values """
        user = User()
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")

    def test_str(self):
        """ test str representation """
        user = User()
        _str_repr = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(user.__str__(), _str_repr)

    def test_save(self):
        """ test save """
        user = User()
        user.save()
        self.assertNotEqual(user.updated_at, user.created_at)


if __name__ == '__main__':
    unittest.main()
