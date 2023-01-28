#!/usr/bin/python3
class User(BaseModel):
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
