#!/usr/bin/python3
class MyModel(BaseModel):
name = "My First Model"
my_number = 89

my_model = MyModel()

print("Instance:",my_model)
my_model.save()
print("After save:",my_model)
my_model_dict = my_model.to_dict()
print("Dictionary :",my_model_dict)
print("JSON of my_model:")
for key, value in my_model_dict.items():
print(f"\t{key} : ({type(value)}) - {value}")
