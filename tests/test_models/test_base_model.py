#!/usr/bin/python3
""" base_model unittest
module contains unit tests for BaseModel class.
"""

import unittest
from datetime import datetime
from time import sleep

from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Test instantiation of BaseModel."""

    def test_base_model_instantiation(self):
        """ BaseModel Test instantiation. """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_base_model_instantiation_no_args(self):
        """ Test instantiation of BaseModel with no args."""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_base_model_instantiation_kwargs(self):
        """ Test BaseModel instantiation with kwargs."""
        b = BaseModel(name="Test")
        self.assertTrue(hasattr(b, "name"))

    def test_base_model_created_date(self):
        """Test created_at attribute."""
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime)

    def test_base_model_created_date2(self):
        """Test type of created_at attribute."""
        b = BaseModel()
        self.assertEqual(type(b.created_at), datetime)

    def test_base_model_updated_date(self):
        """ Test updated_at."""
        b = BaseModel()
        self.assertIsInstance(b.updated_at, datetime)
        self.assertEqual(type(b.updated_at), datetime)

    def test_base_model_create_sleep(self):
        """ Create 2 objects at diff times."""
        b1 = BaseModel()
        sleep(0.1)
        b2 = BaseModel()
        self.assertNotEqual(b1.created_at, b2.created_at)


class TestBaseModelSave(unittest.TestCase):
    """Test BaseModel save|()."""

    def test_base_model_save(self):
        """ Test save(). """
        b = BaseModel()
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_base_model_save_2(self):
        """ Test saving twice. """
        b = BaseModel()
        b.save()
        sleep(0.2)
        b.save()
        self.assertLess(b.created_at, b.updated_at)


class TestBaseModelToDict(unittest.TestCase):
    """ Test to_dict() of BaseModel."""

    def test_base_model_dict_keys(self):
        """ Test keys in dict returned by to_dict()."""
        b = BaseModel()
        _dict = b.to_dict()
        self.assertIn("id", _dict)
        self.assertIn("__class__", _dict)
        self.assertIn("created_at", _dict)
        self.assertIn("updated_at", _dict)


class TestBaseModelStr(unittest.TestCase):
    """ Test str method of BaseModel."""

    def test_base_model_str(self):
        """ Test str method returns string representation."""
        b = BaseModel()
        self.assertEqual(type(str(b)), str)

    def test_base_model_add_attr(self):
        """ Test to_dict contain added attributes."""
        b = BaseModel()
        b.name = "Test"
        b.my_number = 20
        self.assertIn("name", b.to_dict())
        self.assertIn("my_number", b.to_dict())

    def test_base_model_format_date(self):
        """Test format of date in to_dict."""
        b = BaseModel()
        self.assertEqual(type(b.to_dict()["created_at"]), str)
        self.assertEqual(type(b.to_dict()["updated_at"]), str)

    def test_base_model_list_type(self):
        """Test type of dictionary returned by to_dict method."""
        b = BaseModel()
        self.assertEqual(type(b.to_dict()), dict)

    def test_base_model_dict_values(self):
        """Test values in dictionary returned by to_dict method."""
        b = BaseModel()
        _dict = b.to_dict()
        self.assertEqual(type(_dict["id"]), str)
        self.assertEqual(type(_dict["__class__"]), str)
        self.assertEqual(type(_dict["created_at"]), str)
        self.assertEqual(type(_dict["updated_at"]), str)

    def test_base_model_full_dict(self):
        """Test full dict returned by to_dict method."""
        b = BaseModel()
        b.name = "Test"
        b.my_number = 41
        _dict = b.to_dict()
        self.assertEqual(type(_dict), dict)
        self.assertIn("name", _dict)
        self.assertIn("my_number", _dict)
        self.assertIn("id", _dict)
        self.assertIn("__class__", _dict)
        self.assertIn("created_at", _dict)
        self.assertIn("updated_at", _dict)


if __name__ == "__main__":
    unittest.main()
