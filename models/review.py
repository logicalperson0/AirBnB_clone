#!/usr/bin/python3
"""Review class that inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """with place_id, user_id,
    text class attributes
    """
    place_id = ''
    user_id = ''
    text = ''
