#!/usr/bin/python3
""" Review class module - subclass of BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Attributes for Review Class """
    place_id = ""
    user_id = ""
    text = ""
