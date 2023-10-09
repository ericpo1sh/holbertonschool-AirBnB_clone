#!/usr/bin/python3
""" unittest module containing tests for Place subclass of BaseModel """
import os
import unittest
import pycodestyle
from models import storage
from models.place import Place


class TestPlace_class(unittest.TestCase):
    """ Place formatting & initialization tests """
    @classmethod
    def setUp(self):
        self.place1 = Place()
        self.place2 = Place()
        self.place3 = Place(**self.place1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        del self.place1
        del self.place2
        del self.place3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        self.assertTrue(len(Place.__doc__) > 0)

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/place.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_class_attribute_initialization(self):
        self.assertTrue(type(self.place1.user_id) is str)
        self.assertTrue(type(self.place1.name) is str)
        self.assertTrue(type(self.place1.description) is str)
        self.assertTrue(type(self.place1.number_rooms) is int)
        self.assertTrue(type(self.place1.number_bathrooms) is int)
        self.assertTrue(type(self.place1.max_guest) is int)
        self.assertTrue(type(self.place1.price_by_night) is int)
        self.assertTrue(type(self.place1.latitude) is float)
        self.assertTrue(type(self.place1.longitude) is float)
        self.assertTrue(type(self.place1.amenity_ids) is list)
        self.assertTrue(type(self.place2.user_id) is str)
        self.assertTrue(type(self.place2.name) is str)
        self.assertTrue(type(self.place2.description) is str)
        self.assertTrue(type(self.place2.number_rooms) is int)
        self.assertTrue(type(self.place2.number_bathrooms) is int)
        self.assertTrue(type(self.place2.max_guest) is int)
        self.assertTrue(type(self.place2.price_by_night) is int)
        self.assertTrue(type(self.place2.latitude) is float)
        self.assertTrue(type(self.place2.longitude) is float)
        self.assertTrue(type(self.place2.amenity_ids) is list)
        self.assertTrue(type(self.place3.user_id) is str)
        self.assertTrue(type(self.place3.name) is str)
        self.assertTrue(type(self.place3.description) is str)
        self.assertTrue(type(self.place3.number_rooms) is int)
        self.assertTrue(type(self.place3.number_bathrooms) is int)
        self.assertTrue(type(self.place3.max_guest) is int)
        self.assertTrue(type(self.place3.price_by_night) is int)
        self.assertTrue(type(self.place3.latitude) is float)
        self.assertTrue(type(self.place3.longitude) is float)
        self.assertTrue(type(self.place3.amenity_ids) is list)
        self.assertEqual(self.place1.user_id, "")
        self.assertEqual(self.place1.name, "")
        self.assertEqual(self.place1.description, "")
        self.assertEqual(self.place1.number_rooms, 0)
        self.assertEqual(self.place1.number_bathrooms, 0)
        self.assertEqual(self.place1.max_guest, 0)
        self.assertEqual(self.place1.price_by_night, 0)
        self.assertEqual(self.place1.latitude, 0.0)
        self.assertEqual(self.place1.longitude, 0.0)
        self.assertEqual(self.place1.amenity_ids, [])
        self.assertEqual(self.place2.user_id, "")
        self.assertEqual(self.place2.name, "")
        self.assertEqual(self.place2.description, "")
        self.assertEqual(self.place2.number_rooms, 0)
        self.assertEqual(self.place2.number_bathrooms, 0)
        self.assertEqual(self.place2.max_guest, 0)
        self.assertEqual(self.place2.price_by_night, 0)
        self.assertEqual(self.place2.latitude, 0.0)
        self.assertEqual(self.place2.longitude, 0.0)
        self.assertEqual(self.place2.amenity_ids, [])
        self.assertEqual(self.place3.user_id, "")
        self.assertEqual(self.place3.name, "")
        self.assertEqual(self.place3.description, "")
        self.assertEqual(self.place3.number_rooms, 0)
        self.assertEqual(self.place3.number_bathrooms, 0)
        self.assertEqual(self.place3.max_guest, 0)
        self.assertEqual(self.place3.price_by_night, 0)
        self.assertEqual(self.place3.latitude, 0.0)
        self.assertEqual(self.place3.longitude, 0.0)
        self.assertEqual(self.place3.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
