#!/usr/bin/python3
import cmd
import sys
import models

class HBNB(cmd.Cmd):
"""The 'hbnb' class has the 'prompt' variable and 8 methods:
'quit', 'EOF', 'emptyLine', 'create', 'show', 'destroy', 'all', 'update'.
"""
prompt = '(hbnb) '
obj = models.storage.all()
error_msgs = {
"bad_id": "** no instance found ",
"missing_id": " instance id missing ",
"bad_class": " class doesn't exist ",
"missing_class": " class name missing ",
"missing_value": " value missing ",
"missing_attr": " attribute name missing **"
}
valid_classes = ['BaseModel', 'Amenity', 'City', 'Place', 'Review',
'State', 'User']
def do_quit(self, arg):
    """Quits the program."""
    return True

def do_EOF(self, arg):
    """Exits the program."""
    return True

def emptyline(self):
    """Prevents repetition of previous input."""
    pass

def do_create(self, arg):
    """Creates a new instance of BaseModel, saves it to a JSON file."""
    args = arg.split()
    if len(args) < 1:
        print(self.error_msgs['missing_class'])
    elif args[0] in self.valid_classes:
        if args[0] == 'BaseModel':
            new = models.BaseModel()
        if args[0] == 'Amenity':
            new = models.Amenity()
        if args[0] == 'City':
            new = models.City()
        if args[0] == 'Place':
            new = models.Place()
        if args[0] == 'Review':
            new = models.Review()
        if args[0] == 'State':
            new = models.State()
        if args[0] == 'User':
            new = models.User()
        new.save()
        print('{}'.format(new.id))
    else:
        print(self.error_msgs['bad_class'])

def do_show(self, arg):
    """Prints the string representation of an instance."""
    args = arg.split()
    if len(args) == 0:
        print(self.error_msgs['missing_class'])
    elif args[0] not in self.valid_classes:
        print(self.error_msgs['bad_class'])
    elif len(args) < 2:
        print(self.error_msgs['missing_id'])
    else:
        if args[0] in self.valid_classes:
            models.storage.reload()
            instance_dict = models.storage.all()
            if args[1] not in instance
