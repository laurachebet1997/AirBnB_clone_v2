#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel

s = "HBNB_TYPE_STORAGE"
if s in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class Amenity(BaseModel):
        """This is the class for Amenity
        Attributes:
            name: input name
        """
        name = ""
