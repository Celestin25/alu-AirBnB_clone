#!/usr/bin/python3
"""
This module contains the hbnb class for the command interpreter.
"""
import cmd
import sys
import models

class hbnb(cmd.Cmd):
"""
hbnb class inherits from cmd.Cmd and contains the following variables and methods:
- prompt: the prompt for the command interpreter
- obj: all objects stored in the storage
- errors: a dictionary of error messages
- new_class: list of new class types
- do_quit: quits the program
- do_EOF: exits the program
- emptyline: prevents repetition of previous input
- do_create: creates a new instance and saves it to the JSON file
- do_show: prints the string representation of an instance
- do_destroy: deletes an instance based on its class and ID
- do_all: prints string representation of all instances based on class
"""
prompt = '(hbnb) '
obj = models.storage.all()
errors = {
"badid": "** no instance found ",
"noid": " instance id missing ",
"badclass": " class doesn't exist ",
"noclass": " class name missing ",
"novalue": " value missing ",
"noattr": " attribute name missing **"
}
new_class = ['BaseModel', 'Amenity', 'City', 'Place', 'Review',
'State', 'User']
def do_quit(self, args):
    '''Quits the program.'''
    return True

def do_EOF(self, args):
    '''Exits the program.'''
    return True

def emptyline(self):
    '''Prevents repetition of previous input.'''
    pass

def do_create(self, args):
    '''Creates a new instance and saves it to the JSON file.'''
    args = args.split()
    if len(args) < 1:
        print(self.errors['noclass'])
        return
    class_name = args[0]
    if class_name not in self.new_class:
        print(self.errors['badclass'])
        return
    new_obj = None
    if class_name == 'BaseModel':
        new_obj = models.BaseModel()
    elif class_name == 'Amenity':
        new_obj = models.Amenity()
    elif class_name == 'City':
        new_obj = models.City()
    elif class_name == 'Place':
        new_obj = models.Place()
    elif class_name == 'Review':
        new_obj = models.Review()
    elif class_name == 'State':
        new_obj = models.State()
    elif class_name == 'User':
        new_obj = models.User()
    new_obj.save()
    print('{}'.format(new_obj.id))

def do_show(self, args):
    '''Prints the string representation of an instance.'''
    args = args.split()
    if len(args) < 1:
        print(self.errors['noclass'])
        return
