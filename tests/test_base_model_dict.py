#!/usr/bin/python3

from models.base_model import BaseModel

# Create an instance of the BaseModel class and assign values to its attributes
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89

# Print the id of the instance, the instance itself, and the type of the 'created_at' attribute
print(my_model.id)
print(my_model)
print(type(my_model.created_at))

# Convert the instance to a dictionary
my_model_json = my_model.to_dict()

# Print the dictionary and its key-value pairs
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

# Create a new instance of the BaseModel class using the previous dictionary
my_new_model = BaseModel(**my_model_json)

# Print the id of the new instance, the new instance itself, and the type of the 'created_at' attribute
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

# Compare the two instances
print(my_model is my_new_model)
