#!/usr/bin/python3
""" unittest module containing tests for BaseModel class """
import unittest
from models.base_model import BaseModel


class TestBaseModel_init(unittest.TestCase):
    """ BaseModel __init__ method tests """
    def setUp(self):
        self.mod1 = BaseModel()
        self.mod2 = BaseModel()

    def tearDown(self):
        del self.mod1
        del self.mod2

    def test_doc_string(self):
        self.assertTrue(len(BaseModel.__doc__) > 0)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 0)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 0)
        self.assertTrue(len(BaseModel.save.__doc__) > 0)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 0)

    def test_base_model_with_argument(self):
        with self.assertRaises(TypeError):
            BaseModel(1)

    def test_base_model_datetime_attributes(self):
        self.assertEqual(self.mod1.created_at, self.mod1.updated_at)

    def test_id_initialization(self):
        self.assertEqual(len(self.mod1.id), 36)


class TestBaseModel_str(unittest.TestCase):
    """ BaseModel __str__ method tests """
    def setUp(self):
        self.mod1 = BaseModel()

    def tearDown(self):
        del self.mod1

    def test_base_model_str(self):
        self.assertEqual(
            str(self.mod1),
            f"[{self.mod1.__class__.__name__}] \
({self.mod1.id}) {self.mod1.__dict__}"
        )


class TestBaseModel_save(unittest.TestCase):
    """ BaseModel save method tests """
    def setUp(self):
        self.mod1 = BaseModel()

    def tearDown(self):
        del self.mod1

    def test_save_with_argument(self):
        with self.assertRaises(TypeError):
            self.mod1.save(1)


class TestBaseModel_to_dict(unittest.TestCase):
    """ BaseModel to_dict method tests """
    def setUp(self):
        self.mod1 = BaseModel()

    def tearDown(self):
        del self.mod1

    def test_to_dict_with_argument(self):
        with self.assertRaises(TypeError):
            self.mod1.to_dict(1)


if __name__ == "__main__":
    unittest.main()
