#!/usr/bin/python3
"""describes city"""

from models.base_model import Basemodel


class City(Basemodel):
    """ describe a city your searching"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
