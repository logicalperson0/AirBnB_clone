#!/usr/bin/python3
"""Class that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity


class FileStorage:
    """Class that serializes and deserializes from a json file
    """
    __file_path = "bnb.json"
    __objects = {}

    """dicts = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'Review': Review, 'State': State, 'City': City,
                'Amenity': Amenity}"""

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

        for k, v in self.__objects.items():
            dicts[k] = v.to_dict()

        with open(FileStorage.__file_path, "w") as to_file:
            json.dump(dicts, to_file)

    def reload(self):
        """deserializes the JSON file to __objects if it exists"""
        """from models.base_model import BaseModel"""

        dicts = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                 'Review': Review, 'State': State, 'City': City,
                 'Amenity': Amenity}

        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, "r") as from_file:
                js = json.load(from_file)
                for k, v in js.items():
                    self.__objects[k] = dicts[v["__class__"]](**v)
