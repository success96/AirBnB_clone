#!/usr/bin/python3
"""This script is the base model to generate a dictionary representation"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:

    """Class from which all other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """Initializes the  instance attributes"""


        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
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

    def _str_(self):
        """Returns string representation"""
        return format(type(self). _class.name, self.id, self.dict_)



    def save(self):
            """Updates the public instance attribute updated_at with the current date and time."""
            self.updated_at = datetime.now()


    def to_dict(self):

            """returns a dictionary containing keys/values of _dict_"""

            copy_dict = self._dict_.copy()
            copy_dict["_class"] = type(self).class_
            copy_dict["created_at"] = copy_dict["created_at"].isoformat()
            copy_dict["updated_at"] = copy_dict["updated_at"].isoformat()
            return copy_dict
