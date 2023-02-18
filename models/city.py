#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """A ciity

    Attributes:
        state_id: string -empty string: it will be State.id
        name: string - empty string
    """

    state_id = ""
    name = ""
