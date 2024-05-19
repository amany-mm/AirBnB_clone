#!/usr/bin/python3
""" Class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """ Serializes and deserialize instances to JSON
        __file_path: json file path
        __objects: objects dict
    """

    def __init__(self):
        """ int
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ returns a dict of all objects."""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        _dict = {}
        with open(self.__file_path, 'w') as f:
            for obj in self.__objects.values():
                key = obj.__class__.__name__ + "." + obj.id
                _dict[key] = obj.to_dict()
            json.dump(_dict, f)

    def reload(self):
        """ deserializes JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as f:
                my_dict = json.load(f)

            for key, value in my_dict.items():
                _obj = key.split('.')
                class_name = _obj[0]

                self.new(eval("{}".format(class_name))(**value))

        except FileNotFoundError:
            pass
