#!/usr/bin/python3
"""describes a state"""
from models.base_model import Basemodel


class State(Basemodel):
    """ to create a state"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
