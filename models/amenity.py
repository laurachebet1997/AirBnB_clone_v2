#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel

s = "HBNB_TYPE_STORAGE"
class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    name = ""
