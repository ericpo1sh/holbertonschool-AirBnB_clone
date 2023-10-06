#!/usr/bin/python3
""" unittest module containing tests for BaseModel class """
import unittest
import pycodestyle
from genericpath import exists
from models.base_model import BaseModel


class TestBaseModel_init(unittest.TestCase):
    """ BaseModel __init__ method tests """
    def setUp(self):
        self.mod1 = BaseModel()
        self.mod2 = BaseModel()
        self.mod3 = BaseModel(**self.mod1.to_dict())

    def tearDown(self):
        del self.mod1
        del self.mod2

    def test_doc_string(self):
        self.assertTrue(len(BaseModel.__doc__) > 0)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 0)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 0)
        self.assertTrue(len(BaseModel.save.__doc__) > 0)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 0)

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/base_model.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_id_initialization(self):
        self.assertTrue(self.mod1.id, exists)
        self.assertTrue(self.mod2.id, exists)
        self.assertTrue(type(self.mod1.id) is str)
        self.assertTrue(type(self.mod2.id) is str)
        self.assertEqual(len(self.mod1.id), 36)
        self.assertEqual(len(self.mod2.id), 36)
        self.assertNotEqual(self.mod1.id, self.mod2.id)

    def test_created_at_initialization(self):
        self.assertTrue(self.mod1.created_at, exists)
        self.assertTrue(self.mod2.created_at, exists)
        self.assertNotEqual(self.mod1.created_at, self.mod2.created_at)

    def test_updated_at_initialization(self):
        self.assertTrue(self.mod1.updated_at, exists)
        self.assertTrue(self.mod2.updated_at, exists)
        self.assertEqual(self.mod1.created_at, self.mod1.updated_at)
        self.assertEqual(self.mod2.created_at, self.mod2.updated_at)
        self.assertNotEqual(self.mod1.updated_at, self.mod2.updated_at)

    def test_init_kwargs_direct(self):
        kwargs_model = BaseModel(id=2147483647)
        self.assertEqual(kwargs_model.id, 2147483647)

    def test_init_kwargs_from_dict(self):
        self.assertEqual(self.mod3.id, self.mod1.id)
        self.assertEqual(self.mod3.created_at, self.mod1.created_at)
        self.assertEqual(self.mod3.updated_at, self.mod1.updated_at)
        self.assertEqual(self.mod3.__class__, self.mod3.__class__)

    def test_init_args(self):
        args_model = BaseModel([2, 4, 8, 16])
        self.assertNotIn('[2, 4, 8, 16]', args_model.__dict__.items())


class TestBaseModel_str(unittest.TestCase):
    """ BaseModel __str__ method tests """
    def setUp(self):
        self.mod1 = BaseModel()

    def tearDown(self):
        del self.mod1

    def test_base_model_str(self):
        self.assertEqual(
            str(self.mod1),
            "[{}] ({}) {}".format(
                self.mod1.__class__.__name__,
                self.mod1.id,
                self.mod1.__dict__,
            )
        )
        self.assertEqual(
            self.mod1.__str__(),
            "[{}] ({}) {}".format(
                self.mod1.__class__.__name__,
                self.mod1.id,
                self.mod1.__dict__,
            )
        )


class TestBaseModel_save(unittest.TestCase):
    """ BaseModel save method tests """
    def setUp(self):
        self.mod1 = BaseModel()
        self.mod1.save()

    def tearDown(self):
        del self.mod1

    def test_save_with_argument(self):
        with self.assertRaises(TypeError):
            self.mod1.save(1)

    def test_save(self):
        self.assertNotEqual(self.mod1.updated_at, self.mod1.created_at)
        self.assertTrue(self.mod1.created_at < self.mod1.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """ BaseModel to_dict method tests """
    def setUp(self):
        self.mod1 = BaseModel()
        self.mod1_dict = self.mod1.to_dict()

    def tearDown(self):
        del self.mod1

    def test_to_dict_with_argument(self):
        with self.assertRaises(TypeError):
            self.mod1.to_dict(1)

    def test_to_dict_success(self):
        self.assertTrue(self.mod1_dict, exists)
        self.assertTrue(type(self.mod1_dict) is dict)

    def test_to_dict_keys(self):
        self.assertIn(
            '__class__',
            self.mod1_dict
        )
        self.assertIn(
            'created_at',
            self.mod1_dict
        )
        self.assertIn(
            'updated_at',
            self.mod1_dict
        )
        self.assertIn(
            'id',
            self.mod1_dict
        )

    def test_to_dict_values(self):
        self.assertEqual(
            self.mod1_dict['__class__'],
            'BaseModel'
        )
        self.assertEqual(
            self.mod1_dict['__class__'],
            self.mod1.__class__.__name__
        )
        self.assertEqual(
            self.mod1_dict['created_at'],
            self.mod1.created_at.isoformat()
        )
        self.assertEqual(
            self.mod1_dict['updated_at'],
            self.mod1.updated_at.isoformat()
        )
        self.assertEqual(self.mod1_dict['id'], self.mod1.id)


if __name__ == "__main__":
    unittest.main()
