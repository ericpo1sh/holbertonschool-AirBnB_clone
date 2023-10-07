#!/usr/bin/python3
""" FileStorage class module """
import json
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage class definitions """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns __objects dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ adds new object to dictionary with obj.id as key """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serialization of __objects to JSON file at __file_path location """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as outfile:
            json.dump(obj_dict, outfile)

    def reload(self):
        """ deserialization to __objects from saved JSON file, if exists """
        try:
            with open(FileStorage.__file_path, "r") as infile:
                obj_dict = json.load(infile)
                for key, value in obj_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
