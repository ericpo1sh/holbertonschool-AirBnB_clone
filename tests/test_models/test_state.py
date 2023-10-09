#!/usr/bin/python3
""" unittest module containing tests for State subclass of BaseModel """
import os
import unittest
import pycodestyle
from models import storage
from models.state import State


class TestState_class(unittest.TestCase):
    """ State formatting & initialization tests """
    @classmethod
    def setUp(self):
        """ preparation method to be performed before each test """
        self.state1 = State()
        self.state2 = State()
        self.state3 = State(**self.state1.to_dict())
        storage.save()

    @classmethod
    def tearDown(self):
        """ cleanup method to be performed following each test """
        del self.state1
        del self.state2
        del self.state3
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_doc_string(self):
        """ tests module docstring """
        self.assertTrue(len(State.__doc__) > 0)

    def test_pycodestyle(self):
        """ tests module pycodestyle formatting standard compliance """
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/state.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_class_attribute_initialization(self):
        """ verifies attributes initialized with correct value & type """
        self.assertTrue(type(self.state1.name) is str)
        self.assertTrue(type(self.state2.name) is str)
        self.assertTrue(type(self.state3.name) is str)
        self.assertEqual(self.state1.name, "")
        self.assertEqual(self.state2.name, "")
        self.assertEqual(self.state3.name, "")


if __name__ == "__main__":
    unittest.main()
