#!/usr/bin/python3
""" This Module contains UnitTests for the BaseModel Class """
import unittest
from models.base_model import BaseModel


class TestBaseModelInit(unittest.TestCase):
    """ This Test Class tests the BaseModel constructor """

    def test_base_model_constructor(self):
        with self.assertRaises(TypeError):
            BaseModel(1)

    def test_save_method(self):
        with self.assertRaises(TypeError):
            b1 = BaseModel()
            b1.save(1)

    def test_to_dict_method(self):
        with self.assertRaises(TypeError):
            b1 = BaseModel()
            b1.to_dict(1)
