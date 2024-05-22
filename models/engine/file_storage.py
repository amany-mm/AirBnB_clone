#!/usr/bin/python3
""" Class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity


class FileStorage:
    """Serializes and deserialize instances to JSON"""

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "City": City, "State": State, "Amenity": Amenity,
                  "Review": Review,
                  }

    def all(self):
        """ returns a dict of all objects.
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self, obj=None):
        """ serializes __objects to the JSON file (path: __file_path)
        """
        _dict = {}
        with open(self.__file_path, 'w') as f:
            for obj in self.__objects.values():
                key = obj.__class__.__name__ + "." + obj.id
                _dict[key] = obj.to_dict()
            json.dump(_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                new_object = json.load(f)

            for key, val in new_object.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
