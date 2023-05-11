#!/usr/bin/python3
"""Class that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """Class that serializes and deserializes from a json file
    """
    __file_path = "bnb.json"
    __objects = {}

    def all(self):
        """returns the dict __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key"""
        obj_key = obj.__class__.__name__ + '.' + obj.id

        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dicts = {}

        for k, v in FileStorage.__objects.items():
            dicts[k] = v.to_dict()

        with open(FileStorage.__file_path, "w") as to_file:
            json.dump(dicts, to_file)

    def reload(self):
        """deserializes the JSON file to __objects if it exists"""
        from models.base_model import BaseModel
        dicts = {'BaseModel': BaseModel}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, "r") as from_file:
                js = json.load(from_file)
                for k in js:
                    self.__objects[k] = dicts[js[k]["__class__"]](**js[k])
