#!/usr/bin/python3
""" BaseModel module """
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ definitions for BaseModel class """
    def __init__(self):
        """ instantiation of BaseModel object """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ string representation of BaseModel object """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates updated_at attribute with current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns __dict__ keys & values of BaseModel instance """
        inst_dict = self.__dict__.copy()
        inst_dict.update({
            'created_at': datetime.isoformat(self.created_at),
            'updated_at': datetime.isoformat(self.updated_at),
            '__class__': self.__class__.__name__
        })
        return inst_dict
