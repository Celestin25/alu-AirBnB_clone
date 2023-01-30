#!/usr/bin/python3
"""
This module contains the 'hbnb' class for the command interpreter.
"""
import cmd
import sys
import models

class hbnb(cmd.Cmd):
"""The 'hbnb' class, derived from 'cmd.Cmd', with the following features:
- A prompt
- Eight methods: 'quit', 'EOF', 'emptyLine', 'create', 'show', 'destroy', 'all', 'update'
- error messages stored in 'errors' dictionary
- list of available classes in 'new_class'
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
def do_quit(self, arg):
    '''Exit the program.'''
    return True

def do_EOF(self, arg):
    '''Exit the program.'''
    return True

def emptyline(self):
    '''Avoid repeating previous input.'''
    pass

def do_create(self, arg):
    '''Create a new instance of specified class and save it to JSON file.'''
    args = arg.split()
    if not args:
        print(self.errors['noclass'])
    elif args[0] in self.new_class:
        new = getattr(models, args[0])()
        new.save()
        print('{}'.format(new.id))
    else:
        print(self.errors['badclass'])

def do_show(self, arg):
    '''Show the string representation of an instance with given class and id.'''
    args = arg.split()

    if not args:
        print(self.errors['noclass'])
    elif args[0] not in self.new_class:
        print(self.errors['badclass'])
    elif len(args) < 2:
        print(self.errors['noid'])
    else:
        models.storage.reload()
        instances = models.storage.all()
        if args[1] not in instances:
            print(self.errors['badid'])
        else:
            instance = instances[args[1]]
            if args[0] in str(instance):
                print(instance)

def do_destroy(self, arg):
    '''Delete an instance with given class and id.'''
    args = arg.split()

    if not args:
        print(self.errors['noclass'])
    elif args[0] not in self.new_class:
        print(self.errors['badclass'])
    elif len(args) < 2:
        print(self.errors['noid'])
    else:
        models.storage.reload()
        instances =
