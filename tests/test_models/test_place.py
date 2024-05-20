#!/usr/bin/python3
""" Place model test module """
import os
import unittest
from time import sleep
from datetime import datetime

import models
from models.place import Place


class TestPlaceInit(unittest.TestCase):
    """ Test Place model Init """

    def test_no_args(self):
        """ test no args """
        self.assertEqual(Place, type(Place()))

    def test_place_init_stored_in_objects(self):
        """ test place init stored in objects  """
        self.assertIn(Place(), models.storage.all().values())

    def test_place_id_str(self):
        """ test place id str """
        self.assertEqual(str, type(Place().id))

    def test_init_datetime(self):
        """ test_init_datetime """
        self.assertEqual(datetime, type(Place().created_at))
        self.assertEqual(datetime, type(Place().updated_at))

    def test_init__unique_ids(self):
        """ test_init__unique_ids"""
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_init_created_at(self):
        """ test diff created_at in 2 places"""
        p1 = Place()
        sleep(0.2)
        p2 = Place()
        self.assertLess(p1.created_at, p2.created_at)

    def test_city_id(self):
        """ test_city_id """
        p = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(p))
        self.assertNotIn("city_id", p.__dict__)

    def test_user_id(self):
        """ test_user_id """
        p = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(p))
        self.assertNotIn("user_id", p.__dict__)

    def test_number_rooms(self):
        """ test_number_rooms """
        plc = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(plc))
        self.assertNotIn("number_rooms", plc.__dict__)

    def test_latitude(self):
        """ test_latitude """
        p = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(p))
        self.assertNotIn("latitude", p.__dict__)

    def test_amenity_ids(self):
        """ test_amenity_ids"""
        p = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(p))
        self.assertNotIn("amenity_ids", p.__dict__)

    def test_kwargs_None(self):
        """ test_kwargs_None """
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        """ test_kwargs """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        p = Place(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(p.id, "123")
        self.assertEqual(p.created_at, dt)
        self.assertEqual(p.updated_at, dt)

    def test_args_none(self):
        """ test_args_none """
        plc = Place(None)
        self.assertNotIn(None, plc.__dict__.values())


class TestSave(unittest.TestCase):
    """ Test  Place model"""

    @classmethod
    def setUpClass(cls):
        """ setUpClass """
        try:
            os.rename("file.json", "other")
        except IOError:
            pass

    def tearDown(self):
        """ tearDown """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("other", "file.json")
        except IOError:
            pass

    def test_save(self):
        """ test save one """
        p = Place()
        sleep(0.1)
        first_updated_at = p.updated_at
        p.save()
        self.assertLess(first_updated_at, p.updated_at)

    def test_save_no_args(self):
        """ test_save_no_args """
        plc = Place()
        with self.assertRaises(TypeError):
            plc.save(None)

    def test_place_save_update(self):
        """ save update"""
        p = Place()
        p.save()
        p_id = "Place." + p.id
        with open("file.json", "r", encoding="utf-8") as f:
            self.assertIn(p_id, f.read())


class TestStr(unittest.TestCase):
    def test_place_str_method(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        p = Place()
        p.id = "111111111"
        p.created_at = p.updated_at = dt
        p_str = p.__str__()
        self.assertIn("[Place] (111111111)", p_str)
        self.assertIn("'id': '111111111'", p_str)
        self.assertIn("'created_at': " + dt_repr, p_str)
        self.assertIn("'updated_at': " + dt_repr, p_str)


class TestToDict(unittest.TestCase):
    """ test to_dict()"""

    def test_type(self):
        """ test_type """
        self.assertTrue(dict, type(Place().to_dict()))

    def test_no_args(self):
        """ test_no_args """
        plc = Place()
        with self.assertRaises(TypeError):
            plc.to_dict(None)

    def test_to_dict(self):
        """ test_to_dict """
        dt = datetime.today()
        plc = Place()
        plc.id = "111111"
        plc.created_at = plc.updated_at = dt
        tdict = {
            'id': '111111',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(plc.to_dict(), tdict)

    def test_added_attr(self):
        """ test_added_attr """
        plc = Place()
        plc.middle_name = "Test"
        plc.my_number = 20
        self.assertEqual("Test", plc.middle_name)
        self.assertIn("my_number", plc.to_dict())

    def test_to_dict_keys(self):
        """ test if dict have right keys """
        plc = Place()
        self.assertIn("id", plc.to_dict())
        self.assertIn("created_at", plc.to_dict())
        self.assertIn("updated_at", plc.to_dict())
        self.assertIn("__class__", plc.to_dict())

    def test_str_attr(self):
        """ test if attributes are str type """
        plc = Place()
        pl_dict = plc.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_class_attr(self):
        """ test if attributes are str type """
        plc = Place()
        pl_dict = plc.to_dict()
        self.assertEqual("Place", pl_dict["__class__"])

    def test_class_atr(self):
        """ test if attributes are str type """
        plc = Place()
        pl_dict = plc.to_dict()
        self.assertEqual("Place", pl_dict["__class__"])


if __name__ == "__main__":
    unittest.main()
