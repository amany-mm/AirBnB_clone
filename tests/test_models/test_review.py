#!/usr/bin/python3
""" Review model test module """
import os
import unittest
from datetime import datetime
from time import sleep

import models
from models.review import Review


class TestReviewInit(unittest.TestCase):
    """Test Review model Init"""

    def test_no_args(self):
        """test_no_args"""
        self.assertEqual(Review, type(Review()))

    def test_no_kwargs(self):
        """ test_no_kwargss"""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_unused_args(self):
        """ test unused argas"""
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_kwargs(self):
        """ test_kwargs """
        dtt = datetime.today()
        dt_iso = dtt.isoformat()
        rev = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rev.id, "345")
        self.assertEqual(rev.created_at, dtt)
        self.assertEqual(rev.updated_at, dtt)

    def test_new_instance_stored_in_objects(self):
        """ test new instance stored in objects"""
        self.assertIn(Review(), models.storage.all().values())

    def test_id(self):
        """ test if id is public attribute """
        self.assertEqual(str, type(Review().id))

    def test_dates(self):
        """ test_review_instantiation_dates"""
        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id(self):
        """ test_place_id"""
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_user_id(self):
        """ test_user_id """
        rev = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

    def test_text(self):
        """ test_text """
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_unique_ids(self):
        """ test unique ids for two reviews"""
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_created_at(self):
        """ test two reviews different created at"""
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def test_review_instantiation_reviews_2(self):
        """ test two reviews different updated"""
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)


class TestSave(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    @classmethod
    def setUpClass(cls):
        """ setUpClass """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """ tearDown """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_one(self):
        """ test_save_one"""
        rev = Review()
        sleep(0.05)
        updated_at_1st = rev.updated_at
        rev.save()
        self.assertLess(updated_at_1st, rev.updated_at)

    def test_save_two(self):
        """ test_save_two """
        rev = Review()
        sleep(0.05)
        updated_at_1st = rev.updated_at
        rev.save()
        updated_at_2nd = rev.updated_at
        self.assertLess(updated_at_1st, updated_at_2nd)
        sleep(0.05)
        rev.save()
        self.assertLess(updated_at_2nd, rev.updated_at)

    def test_no_args(self):
        """ test_no_args """
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def test_save_to_json_file(self):
        """ update file """
        rev = Review()
        rev.save()
        rev_id = "Review." + rev.id
        with open("file.json", "r") as f:
            self.assertIn(rev_id, f.read())


class TestStr(unittest.TestCase):
    """ Test Str"""

    def test_review_str_(self):
        """ test review __str__ representation """
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)


class TestToDict(unittest.TestCase):
    """testing to_dict() of the Review class."""

    def test_to_dict(self):
        """ test_to_dict """
        self.assertTrue(dict, type(Review().to_dict()))

    def test_no_args(self):
        """ test pass no args"""
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)

    def test_datetime(self):
        """ test datetime attrs as str"""
        rev = Review()
        rv_dict = rev.to_dict()
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_to_dict_output(self):
        """ test output"""
        dtt = datetime.today()
        rev = Review()
        rev.id = "121212"
        rev.created_at = rev.updated_at = dtt
        _dict = {
            'id': '121212',
            '__class__': 'Review',
            'created_at': dtt.isoformat(),
            'updated_at': dtt.isoformat(),
        }
        self.assertDictEqual(rev.to_dict(), _dict)

    def test_keys(self):
        """ test correct keys"""
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())

    def test_added_attrs(self):
        """ test added attrs """
        rev = Review()
        rev.middle_name = "Test"
        rev.my_number = 98
        self.assertEqual("Test", rev.middle_name)
        self.assertEqual(98, rev.my_number)
        self.assertIn("my_number", rev.to_dict())


if __name__ == "__main__":
    unittest.main()
