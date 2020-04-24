#!/usr/bin/python3
""" new engine of storage """
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """ class DBStorage for engine """
    """CLASSES = {
        'Amenity': amenity,
        'City': city,
        'Place': place,
        'Review': review,
        'State': state,
        'User': user
    }"""

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
            if type(cls) is str:
                cls = eval(cls)
            r_query = self.__session.query(cls)
            for ins in r_query:
                ins_name = "{}.{}".format(type(ins).__name__, ins.id)
                new_dict[ins_name] = ins
        else:
            new_list = [State, City, User, Place, Review, Amenity]
            for c in new_list:
                r_query = self.__session.query(c)
                for ins in r_query:
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
