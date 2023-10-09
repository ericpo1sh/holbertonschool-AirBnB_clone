#!/usr/bin/python3
""" FileStorage class module """
import json
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage class definitions """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns __objects dictionary """
        return self.__objects

    def new(self, obj):
        """ adds new object to dictionary with obj.id as key """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serialization of __objects to JSON file at __file_path location """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as outfile:
            json.dump(obj_dict, outfile)

    def reload(self):
        """ deserialization to __objects from saved JSON file, if exists """
        try:
            with open(self.__file_path, "r") as infile:
                obj_dict = json.load(infile)
                for key, value in obj_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
