#!/usr/bin/python3
""" City model test module """
import unittest
from time import sleep
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ City model test """

    def test_parent(self):
        """ test inheritance """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attrs(self):
        """ test attributes """
        self.assertIn("state_id", City.__dict__)
        self.assertIn("name", City.__dict__)

    def test_str(self):
        """ test str """
        _city = City()
        string = "[City] ({}) {}".format(_city.id, _city.__dict__)
        self.assertEqual(string, str(_city))

    def test_save(self):
        """ test save """
        _city = City()
        _city.save()

        sleep(0.1)
        _city.save()
        self.assertNotEqual(_city.updated_at, _city.created_at)

    def test_to_dict(self):
        """ test to_dict() """
        _city = City()
        new_dict = _city.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertIn("to_dict", dir(_city))

    def test_docs(self):
        """ test docs """
        self.assertIsNotNone(City.__doc__)


if __name__ == "__main__":
    unittest.main()
