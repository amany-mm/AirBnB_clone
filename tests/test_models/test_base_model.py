#!/usr/bin/python3
"""
BaseModel class unittest
"""
import os
import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    BaseModel test
    """
    @classmethod
    def setUpClass(cls):
        """setUpClass
        """
        cls.base = BaseModel()
        cls.base.name = "Test"
        cls.base.my_number = 5

    @classmethod
    def tearDownClass(cls):
        """tearDownClass test.
        """
        del cls.base

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style(self):
        """
        pep8 style test.
        """
        _style = pep8.StyleGuide(quiet=True)

        f_style = _style.check_files(['models/base_model.py'])
        self.assertEqual(f_style.total_errors, 0, "fix pep8")

    def test_func(self):
        """
        Test doc func.
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_attrs(self):
        """
        Test attr
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "save"))

    def test_init(self):
        """
        test initializer
        """
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save(self):
        """
        tests saving of json file
        """
        self.base.save()
        self.assertNotEqual(self.base.updated_at, self.base.created_at)

    def test_to_dict(self):
        """
        tests dict instance objects.
        """
        base_dict = self.base.to_dict()

        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')


if __name__ == "__main__":
    unittest.main()
