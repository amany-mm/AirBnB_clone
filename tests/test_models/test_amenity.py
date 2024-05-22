#!/usr/bin/python3
""" Amenity model test module """

import os
import unittest
import models
from datetime import datetime
from models.amenity import Amenity
from time import sleep


class TestAmenity(unittest.TestCase):
    """ Amenity model test """

    def test_init_no_args(self):
        """ test init no args """
        self.assertEqual(Amenity, type(Amenity()))

    def test_args_unused(self):
        """ test args unused """
        amen = Amenity(None)
        self.assertNotIn(None, amen.__dict__.values())

    def test_init_kwargs(self):
        """ test init kwargs """
        amen_date = datetime.today()
        date_iso = amen_date.isoformat()
        amen = Amenity(id="123", created_at=date_iso, updated_at=date_iso)

        self.assertEqual(amen.id, "123")
        self.assertEqual(amen.created_at, amen_date)
        self.assertEqual(amen.updated_at, amen_date)

    def test_init_kwargs_none(self):
        """ test init kwargs none """
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_init_stored_in_objs(self):
        """ test init stored in objs """
        self.assertIn(Amenity(), models.storage.all().values())

    def test_dates_type(self):
        """ test dates type"""
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_attr(self):
        """ test attr """
        amen = Amenity()
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amen.__dict__)

    def test_created_at(self):
        """ test_created_at """
        amen = Amenity()
        sleep(0.1)
        amen2 = Amenity()
        self.assertLess(amen.created_at, amen2.created_at)

    def test_amenities_str(self):
        """ test_amenities_str """
        amen_date = datetime.today()
        date_repr = repr(amen_date)
        amen = Amenity()
        amen.id = "121212"
        amen.created_at = amen.updated_at = amen_date

        amen_str = amen.__str__()
        self.assertIn("[Amenity] (121212)", amen_str)
        self.assertIn("'id': '121212'", amen_str)
        self.assertIn("'created_at': " + date_repr, amen_str)
        self.assertIn("'updated_at': " + date_repr, amen_str)


if __name__ == '__main__':
    unittest.main()
