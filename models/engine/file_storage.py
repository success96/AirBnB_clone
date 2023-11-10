#!/usr/bin/python3
"""
This script contains fileStorage class for serialization and deserialization
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes 
    JSON files to instances
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """This method returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This method sets in __objects the obj with key <obj class name>.id"""
        objectClassName = obj.__class__.__name__
        FileStorage.__objects[f"{objectClassName}.{obj.id}"] = obj

    def save(self):
        """This method serializes __objects to the JSON file (path: __file_path)"""
        odict = FileStorage.__objects
        objectDict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objectDict, f)

    def reload(self):
        """This methode deserializes the JSON file to __objects
           only if the JSON file (__file_path) exists.
           If the file doesn't exist no
           exception should be raised"""
        try:
            with open(FileStorage.__file_path) as f:
                objectDict = json.load(f)
                for o in objectDict.values():
                    className = o["__class__"]
                    del o["__class__"]
                    self.new(eval(className)(**o))
        except FileNotFoundError:
            return
