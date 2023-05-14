#!usr/bin/python3
"""city class that inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that has: state_id,
    name attributes
    """
    state_id = ""
    name = ""
