#!/usr/bin/python3
"""Module Storage """

import json


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
