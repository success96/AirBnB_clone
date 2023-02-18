#!/usr/bin/python3
"""The User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User

    Attributes:
        email: The email of the user
        password: User's password
        first_name: User's first name
        last_name: User's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
