#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """Represent an abstracted strage engine

    Attributes:
        __file_path: The name of the file to save object to.
        __objects: A dictionary to store objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        objectClassName = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objectClassName, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        odict = FileStorage.__objects
        objectDict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objectDict, f)

    def reload(self):
        """Deserializes the JSON file to __objects
           only if the JSON file (__file_path) exists
           otherwise, do nothung. If the file doesn't exist
           no exception should be raised"""
        try:
            with open(FileStorage.__file_path) as f:
                objectDict = json.load(f)
                for o in objectDict.values():
                    className = o["__class__"]
                    del o["__class__"]
                    self.new(eval(className)(**o))
        except FileNotFoundError:
            return
