#!/usr/bin/python3
""" unittest module containing tests for Review subclass of BaseModel """
import os
import unittest
import pycodestyle
from models import storage
from models.review import Review


class TestReview_class(unittest.TestCase):
    """ Review formatting & initialization tests """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.review1 = Review()
        self.review2 = Review()
        self.review3 = Review(**self.review1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.review1
        del self.review2
        del self.review3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        """ tests module docstring """
        self.assertTrue(len(Review.__doc__) > 0)

    def test_pycodestyle(self):
        """ tests module pycodestyle formatting standard compliance """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/review.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_class_attribute_initialization(self):
        """ verifies attributes initialized with correct value & type """
        self.assertTrue(type(self.review1.place_id) is str)
        self.assertTrue(type(self.review1.user_id) is str)
        self.assertTrue(type(self.review1.text) is str)
        self.assertTrue(type(self.review2.place_id) is str)
        self.assertTrue(type(self.review2.user_id) is str)
        self.assertTrue(type(self.review2.text) is str)
        self.assertTrue(type(self.review3.place_id) is str)
        self.assertTrue(type(self.review3.user_id) is str)
        self.assertTrue(type(self.review3.text) is str)
        self.assertEqual(self.review1.place_id, "")
        self.assertEqual(self.review1.user_id, "")
        self.assertEqual(self.review1.text, "")
        self.assertEqual(self.review2.place_id, "")
        self.assertEqual(self.review2.user_id, "")
        self.assertEqual(self.review2.text, "")
        self.assertEqual(self.review3.place_id, "")
        self.assertEqual(self.review3.user_id, "")
        self.assertEqual(self.review3.text, "")


if __name__ == "__main__":
    unittest.main()
