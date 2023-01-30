#!/usr/bin/python3
"""
That is the 'console' module.
Console carries the 'hbnb' magnificence, which inherits from the 'cmd.Cmd' magnificence.
This consists of the entry point for the command interpreter.
"""
Import cmd
Import sys
Import fashions


Magnificence hbnb(cmd.Cmd):
    """that is the 'hbnb' class.
    Hbnb incorporates the variable 'spark off'. It also consists of eight techniques:
    'end', 'EOF', 'emptyLine', 'create', 'show', ruin',
    'all', 'update'.
    """
    prompt = '(hbnb) '
    obj = models.Garage.All()
    errors = 
        "badid": "** no example found **",
        "noid": "** example identification lacking **",
        "badclass": "** class doesn't exist **",
        "noclass": "** class name missing **",
        "novalue": "** fee missing **",
        "noattr": "** attribute call missing **"
    
    new_class = ['BaseModel', 'Amenity', 'City', 'Place', 'Review',
                 'State', 'User']

    def do_quit(self, arg):
        '''stop command to go out the program.'''
        go back actual

    def do_EOF(self, arg):
        '''Exits this system.'''
        return authentic

    def emptyline(self):
        '''Prevents repeat of preceding input.'''
        skip

    def do_create(self, arg):
        '''Creates a brand new example of BaseModel, keep to JSON file.'''
        args = arg.Split()
        if len(args) < 1:
            print(self.Errors['noclass'])
        elif args[0] in self.New_class:
            if args[0] == 'BaseModel':
                new = fashions.BaseModel()
            if args[0] == 'Amenity':
                new = models.Amenity()
            if args[0] == 'metropolis':
                new = fashions.City()
            if args[0] == 'region':
                new = fashions.Area()
            if args[0] == 'review':
                new = fashions.Evaluation()
            if args[0] == 'state':
                new = fashions.Kingdom()
            if args[0] == 'user':
                new = fashions.Person()
            new.Save()
            print(''.Layout(new.Id))
        else:
            print(self.Mistakes['badclass'])

    def do_show(self, arg):
        '''Prints the string illustration of an instance'''
        args = arg.Cut up()

        if (len(args) == 0):
            print(self.Mistakes['noclass'])
        elif args[0] now not in self.New_class:
            print(self.Errors['badclass'])
        elif (len(args) < 2):
            print(self.Mistakes['noid'])
        else:
            if args[0] in self.New_class:
                fashions.Garage.Reload()
                new_dict = fashions.Garage.All()
                if args[1] now not in new_dict:
                    print(self.Errors['badid'])
                for key in new_dict:
                    if args[0] in str(new_dict[key]):
                        if args[1] in new_dict.Keys():
                            print(new_dict[args[1]])
                            destroy

    def do_destroy(self, arg):
        '''Deletes an instance based totally on the elegance name and identification,'''
        args = arg.Break up()

        if (len(args) == 0):
            print(self.Errors['noclass'])
        elif args[0] not in self.New_class:
            print(self.Mistakes['badclass'])
        elif (len(args) < 2):
            print(self.Errors['noid'])
        else:
            if args[0] in self.New_class:
                models.Storage.Reload()
                new_dict = models.Storage.All()
                if args[1] not in new_dict:
                    print(self.Errors['badid'])
                else:
                    if args[1] in new_dict.Keys():
                        if args[0] in str(new_dict[args[1]]):
                            del new_dict[args[1]]
                            models.Storage.Save()

    def do_all(self, arg):
        '''Prints string representation of all instances based on class'''
        our_list = []
        args = arg.Split()

        if len(args) > 0:
            if args[0] in self.New_class:
                for i in self.Obj.Keys():
                    if self.Obj[i].__class__.__name__ == args[0]:
                        our_list.Append(str(self.Obj[i]))
                print(our_list)
            else:
                print(self.Mistakes['badclass'])
    def do_update(self, arg):
        '''Updates an example by including or updating characteristic'''
        args = arg.Break up()
        new_dict = fashions.Storage.All()

        if len(args) == zero:
            print(self.Mistakes['noclass'])
        elif args[0] now not in self.New_class:
            print(self.Errors['badclass'])
        elif len(args) < 2:
            print(self.Mistakes['noid'])
        elif args[1] not in new_dict:
            print(self.Mistakes['badid'])
        elif len(args) < 4 not in self.Obj:
            print(self.Errors['novalue'])
        else:
            class_name = args[0]
            user_id = args[1]
            attribute_name = args[2]
            attribute_value = ""
            if (len(args) > 4):
                for i in variety(len(args) - three):
                    attribute_value += (args[i + 3].Replace('"', ''))
                    if i < (len(args) - 4):
                        attribute_value += " "
            else:
                attribute_value = args[3].Update('"', '')
            if class_name in self.New_class:
                (self.Obj[user_id]).__dict__[attribute_name] = attribute_value
                fashions.Storage.Shop()

If __name__ == '__main__':
    hbnb().Cmdloop()
