#!/usr/bin/python3
""" City class module - subclass of BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ Attributes for City Class """
    state_id = ""
    name = ""
