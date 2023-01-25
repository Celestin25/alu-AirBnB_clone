#!/usr/bin/python3
"""
    Contains the definition of the BaseModel class thst defines all common
    attributes and methods for other classes in the AirBnB clone project.
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """Definition of the class BaseModel. Defines all common attributes and
       methods for other classes in the AirBnB project
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class.
           Also recreate a class instance from a dictiornary.
        Attributes:
            id (str) - a unique identification number for each class instance
            created_at (datetime) - a datetime object indicatingt
