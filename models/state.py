#!/usr/bin/python3
"""This is the state class"""
import os
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
import shlex

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """
    class State for manage all states
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    @property
    def cities(self):
        """
        returns a list of city objects with state_id
        from the current state
        """
        all_models = models.storage.all()
        res = []
        list_cities = []
        for key in all_models:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if city[0] == 'City':
                list_cities.append(all_models[key])
        for obj in list_cities:
            if (obj.state_id == self.id):
                res.append(obj)
        return res
