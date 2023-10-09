#!/usr/bin/python3
""" unittest module containing tests for City subclass of BaseModel """
import os
import unittest
import pycodestyle
from models import storage
from models.city import City


class TestCity_class(unittest.TestCase):
    """ City formatting & initialization tests """
    @classmethod
    def setUp(self):
        self.city1 = City()
        self.city2 = City()
        self.city3 = City(**self.city1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        del self.city1
        del self.city2
        del self.city3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        self.assertTrue(len(City.__doc__) > 0)

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/city.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_class_attribute_initialization(self):
        self.assertTrue(type(self.city1.state_id) is str)
        self.assertTrue(type(self.city1.name) is str)
        self.assertTrue(type(self.city2.state_id) is str)
        self.assertTrue(type(self.city2.name) is str)
        self.assertTrue(type(self.city3.state_id) is str)
        self.assertTrue(type(self.city3.name) is str)
        self.assertEqual(self.city1.state_id, "")
        self.assertEqual(self.city1.name, "")
        self.assertEqual(self.city2.state_id, "")
        self.assertEqual(self.city2.name, "")
        self.assertEqual(self.city3.state_id, "")
        self.assertEqual(self.city3.name, "")


if __name__ == "__main__":
    unittest.main()
