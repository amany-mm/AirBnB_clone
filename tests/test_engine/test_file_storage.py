#!/usr/bin/python3
"""
FileStorage class unittest module
"""
import unittest
import models


class TestFileStorage(unittest.TestCase):
    """ TestFileStorage """

    def test_doc(self):
        """ doc test"""
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.__doc__)
        self.assertIsNotNone(
            models.engine.file_storage.FileStorage.all.__doc__)
        self.assertIsNotNone(
            models.engine.file_storage.FileStorage.__init__.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             save.__doc__)
        self.assertIsNotNone(
            models.engine.file_storage.FileStorage.new.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             reload.__doc__)

    def test_class(self):
        """class creation test """
        self.assertIsInstance(models.engine.file_storage.FileStorage(),
                              models.engine.file_storage.FileStorage)

    def test_all(self):
        """test all"""
        self.assertIsNotNone(models.engine.file_storage.FileStorage().all)

    def test_save(self):
        """test save """
        self.assertIsNotNone(models.engine.file_storage.FileStorage().save)

    def test_new(self):
        """test new """
        self.assertIsNotNone(models.engine.file_storage.FileStorage().new)

    def test_reload(self):
        """ test reload """
        self.assertIsNotNone(models.engine.file_storage.FileStorage().reload)

    def test_models_all_method(self):
        """test all() is working"""
        self.assertIsNotNone(models.storage.all())

    def test_all_method(self):
        """test all() is working"""
        self.assertIsNotNone(models.engine.file_storage.FileStorage().all())


if __name__ == '__main__':
    unittest.main()
