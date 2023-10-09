#!/usr/bin/python3
""" unittest module containing tests for Amenity subclass of BaseModel """
import os
import unittest
import pycodestyle
from models import storage
from models.amenity import Amenity


class TestAmenity_class(unittest.TestCase):
    """ Amenity formatting & initialization tests """
    @classmethod
    def setUp(self):
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()
        self.amenity3 = Amenity(**self.amenity1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        del self.amenity1
        del self.amenity2
        del self.amenity3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/amenity.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_class_attribute_initialization(self):
        self.assertTrue(type(self.amenity1.name) is str)
        self.assertTrue(type(self.amenity2.name) is str)
        self.assertTrue(type(self.amenity3.name) is str)
        self.assertEqual(self.amenity1.name, "")
        self.assertEqual(self.amenity2.name, "")
        self.assertEqual(self.amenity3.name, "")


if __name__ == "__main__":
    unittest.main()
