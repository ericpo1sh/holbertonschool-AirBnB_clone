#!/usr/bin/python3
""" User class module - subclass of BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Attributes for User Class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
