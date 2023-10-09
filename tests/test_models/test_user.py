#!/usr/bin/python3
""" unittest module containing tests for User subclass of BaseModel """
import os
import unittest
import pycodestyle
from models import storage
from models.user import User


class TestUser_class(unittest.TestCase):
    """ User formatting & initialization tests """
    @classmethod
    def setUp(self):
        self.usr1 = User()
        self.usr2 = User()
        self.usr3 = User(**self.usr1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        del self.usr1
        del self.usr2
        del self.usr3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        self.assertTrue(len(User.__doc__) > 0)

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/user.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_class_attribute_initialization(self):
        self.assertTrue(type(self.usr1.email) is str)
        self.assertTrue(type(self.usr1.password) is str)
        self.assertTrue(type(self.usr1.first_name) is str)
        self.assertTrue(type(self.usr1.last_name) is str)
        self.assertTrue(type(self.usr2.email) is str)
        self.assertTrue(type(self.usr2.password) is str)
        self.assertTrue(type(self.usr2.first_name) is str)
        self.assertTrue(type(self.usr2.last_name) is str)
        self.assertTrue(type(self.usr3.email) is str)
        self.assertTrue(type(self.usr3.password) is str)
        self.assertTrue(type(self.usr3.first_name) is str)
        self.assertTrue(type(self.usr3.last_name) is str)
        self.assertEqual(self.usr1.email, "")
        self.assertEqual(self.usr1.password, "")
        self.assertEqual(self.usr1.first_name, "")
        self.assertEqual(self.usr1.last_name, "")
        self.assertEqual(self.usr2.email, "")
        self.assertEqual(self.usr2.password, "")
        self.assertEqual(self.usr2.first_name, "")
        self.assertEqual(self.usr2.last_name, "")
        self.assertEqual(self.usr3.email, "")
        self.assertEqual(self.usr3.password, "")
        self.assertEqual(self.usr3.first_name, "")
        self.assertEqual(self.usr3.last_name, "")


if __name__ == "__main__":
    unittest.main()
