#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review

    Attributes:
        place_id: string - empty string
        user_id: string - empty string
        text: string - empty string
    """

    place_id = ""
    user_id = ""
    text = ""
