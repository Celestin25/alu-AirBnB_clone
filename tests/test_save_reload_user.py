#!/usr/bin/python3
"""Test of comment"""

# Import the storage module and the BaseModel and User classes
from models import storage
from models.base_model import BaseModel
from models.user import User

# Retrieve all objects from the storage
all_objs = storage.all()

# Print all objects
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Create a new User
print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"

# Save the new User to the storage
my_user.save()
print(my_user)

# Create a new User 2
print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "Peter"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"

# Save the new User 2 to the storage
my_user2.save()
print(my_user2)
