#!/usr/bin/python3
"""This script is the base model to generate a dictionary representation"""

import uuid
from datetime import datetime
import models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

class BaseModel:
    """Class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """Initializes the  instance attributes"""

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "__class__":
                     pass
                elif key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation"""
        return f"[{self. __class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
            """Updates the public instance attribute updated_at with the current date and time."""
            self.updated_at = datetime.now()
            models.storage.save()

    def to_dict(self):
            """returns a dictionary containing keys/values of _dict_"""

            copy_dict = self.__dict__.copy()
            copy_dict["__class__"] = self.__class__.__name__
            copy_dict["created_at"] = copy_dict["created_at"].isoformat()
            copy_dict["updated_at"] = copy_dict["updated_at"].isoformat()
            return copy_dict
    
