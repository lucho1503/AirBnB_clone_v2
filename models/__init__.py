#!/usr/bin/python3
""" create a instance for apllication """
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import os

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


if STORAGE_TYPE == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
