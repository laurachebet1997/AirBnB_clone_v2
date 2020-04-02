#!/usr/bin/python3
'''
This is the file storage class for AirBnB
'''
import json
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import InvalidRequestError


class DBStorage:
    '''
    serializes instances to a JSON file
    '''
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                environ['HBNB_MYSQL_USER'],
                environ['HBNB_MYSQL_PWD'],
                environ['HBNB_MYSQL_HOST'],
                environ['HBNB_MYSQL_DB']),
            pool_pre_ping=True)
        if 'HBNB_ENV' in environ.keys() and environ['HBNB_ENV'] == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        return a dictionary
        '''
        res = None
        ad = {}
        nl = []
        if clss is None:
            classes = [User, State, City, Amenity, Place, Review]
            for j in classes:
                try:
                    res = self.__session.query(j).all()
                    if res is not None:
                        for i in res:
                            nl.append(i)
                except InvalidRequestError:
                    pass
        else:
            res = self.__session.query(eval(clss)).all()
            if res is not None:
                for i in res:
                    nl.append(i)
        return nl

    def new(self, obj):
        '''
        new obj
        '''
        if j is not None:
            self.__session.add(j)
            self.__session.commit()

    def save(self):
        '''
        JSON file path
        '''
        self.__session.commit()

    def reload(self):
        '''
        JSON file path
        '''
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_fact)

    def delete(self, j=None):
        '''
        delete an object
        '''
        if j is not None:
            self.__session.delete(j)
            self.__session.commit()

    def close(self):
        '''
        close
        '''
        self.__session.remove()
