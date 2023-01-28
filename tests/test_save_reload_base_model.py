#!/usr/bin/python3
"""Test of comment"""

# Import the storage module and the BaseModel class
from models import storage
from models.base_model import BaseModel

# Retrieve all objects from the storage
all_objs = storage.all()

# Print all objects
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Create a new object
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89

# Save the new object to the storage
my_model.save()
print(my_model)
