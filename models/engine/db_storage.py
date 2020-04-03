#!/usr/bin/python3
""" new engine of storage """
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import base_model, amenity, city, place, review, state, user


class DBStorage:
    """ class DBStorage for engine """
    CLASSES = {
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'state': state.State,
        'User': user.User
    }

    """ prepares a engine database """
    __engine = None
    __session = None

    def __init__(self):
        """ prepares the engine of database """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ.get('HBNB_MYSQL_USER'),
                os.environ.get('HBNB_MYSQL_PWD'),
                os.environ.get('HBNB_MYSQL_HOST'),
                os.environ.get('HBNB_MYSQL_DB')))
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ retrieves a dictionary of all objects """
        new_dict = {}
        if cls is not None:
            sess_query = self.__session.query(DBStorage.CLASSES[cls])
            for ins in sess_query:
                ins_name = "{}.{}".format(type(ins).__name__, ins.id)
                new_dict[ins_name] = ins
            return new_dict

        for c in DBStorage.CLASSES.values():
            sess_query = self.__session.query(c)
            for ins in sess_query:
                ins_name = "{}.{}".format(type(ins).__name__, ins.id)
                new_dict[ins_name] = ins
        return new_dict

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def rollback_session(self):
        """ commits all changes of the current database session """
        self.__session.rollback()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ creates all tables in database """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine,
                         expire_on_commit=False))

    def close(self):
        self.__session.close()
