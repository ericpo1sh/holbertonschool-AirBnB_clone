#!/usr/bin/python3
""" unittest module containing tests for BaseModel class """
import os
import unittest
import pycodestyle
from models import storage
from genericpath import exists
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_class(unittest.TestCase):
    """ tests FileStorage class init & formatting related operations """
    def test_doc_string(self):
        self.assertTrue(len(FileStorage.__doc__) > 0)
        self.assertTrue(len(FileStorage.all.__doc__) > 0)
        self.assertTrue(len(FileStorage.new.__doc__) > 0)
        self.assertTrue(len(FileStorage.save.__doc__) > 0)
        self.assertTrue(len(FileStorage.reload.__doc__) > 0)

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/engine/file_storage.py']).total_errors,
            0,
            "Found code style errors (and warnings)."
        )

    def test_call_with_argument(self):
        with self.assertRaises(TypeError):
            FileStorage(1)

    def test_class_attributes_private(self):
        with self.assertRaises(AttributeError):
            print(storage.__objects)
            print(storage.__file_path)

    def test_type(self):
        self.assertTrue(type(storage) is FileStorage)


class TestFileStorage_all(unittest.TestCase):
    """ tests FileStorage all method """
    def setUp(self):
        self.obj = BaseModel()
        storage.save()

    def tearDown(self):
        del self.obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_all(self):
        self.assertTrue(self.obj, exists)
        self.assertIn(
            f'{self.obj.__class__.__name__}.{self.obj.id}',
            storage._FileStorage__objects
        )
        self.assertTrue(type(storage.all()) is dict)
        self.assertTrue(len(storage.all()) > 0)

    def test_all_with_argument(self):
        with self.assertRaises(TypeError):
            storage.all(1)


class TestFileStorage_new(unittest.TestCase):
    """ tests FileStorage new method """
    def setUp(self):
        self.obj = BaseModel()
        storage.save()

    def tearDown(self):
        del self.obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_new(self):
        storage.new(self.obj)
        self.assertIn(
            f'{self.obj.__class__.__name__}.{self.obj.id}',
            storage._FileStorage__objects
        )
        self.assertIn(self.obj, storage.all().values())

    def test_new_excessive_arguments(self):
        with self.assertRaises(TypeError):
            storage.new(self.obj, 6)

    def test_new_undesired_object_type_argument(self):
        with self.assertRaises(AttributeError):
            storage.new(8)
            storage.new({2, 4, 8})


class TestFileStorage_save(unittest.TestCase):
    """ tests FileStorage save method """
    def setUp(self):
        self.obj = BaseModel()
        storage.save()

    def tearDown(self):
        del self.obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save(self):
        self.obj.save()
        self.assertTrue(os.path.exists('file.json'))
        with open("file.json") as file:
            content = file.read()
            self.assertIn(
                f"{self.obj.__class__.__name__}.{self.obj.id}",
                content
            )
            self.assertTrue(len(content) > 0)

    def test_save_with_argument(self):
        with self.assertRaises(TypeError):
            storage.save(1)


class TestFileStorage_reload(unittest.TestCase):
    """ tests FileStorage reload method """
    def setUp(self):
        self.obj = BaseModel()
        storage.save()

    def tearDown(self):
        del self.obj
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_reload(self):
        storage.reload()
        self.assertIn(
            f'{self.obj.__class__.__name__}.{self.obj.id}',
            storage._FileStorage__objects
        )
        self.assertTrue(len(storage.all()) > 0)

    def test_reload_with_argument(self):
        with self.assertRaises(TypeError):
            storage.reload(1)


if __name__ == "__main__":
    unittest.main()
