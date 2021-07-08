#!/usr/bin/python3
"""Module Storage """

from models.base_model import BaseModel
import json
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        JS = {}
        for i in self.__objects:
            JS[i] = self.__objects[i].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(JS, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """

        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj = json.load(f)
            for k, v in obj.items():
                class_name = k.split('.')[0]
                self.__objects[k] = eval(class_name)(**v)
        except:
            pass
