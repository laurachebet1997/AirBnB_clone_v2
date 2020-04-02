#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ
import models
from uuid import uuid4

s = "HBNB_TYPE_STORAGE"
if s in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class State(BaseModel, Base):
        '''
        state class
        '''
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")

        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for i, j in kwargs.items():
                setattr(self, i, j)
else:
    class State(BaseModel):
        '''
        state class
        '''
        name = ""

        @property
        def cities(self):
            all_city = models.storage.all(City)
            liste = []
            keys = all_city.items()
            for i, j in keys:
                if "City" == i[0:4] and j.state_id == self.id:
                    liste.append(j)
            return(liste)
