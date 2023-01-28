import argparse
import pickle
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand:
    """Defines command interpreter.
    """

    __all_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='HBNB Command Line Interface')
        self.parser.add_argument('class_name', choices=self.__all_classes,
                                 help='Name of the class to create instance')
        self.parser.add_argument('id', help='ID of the class instance')

    def create(self):
        """
            Creates a new instance of a class,
            saves it (to the file) and prints the id.
        """
        args = self.parser.parse_args()
        new_object = eval(args.class_name + "()")
        new_object.save()
        print(new_object.id)
        with open('storage.pkl', 'wb') as f:
            pickle.dump(storage, f)

    def show(self):
        """
        Display string representation of a class instance of given id.
        """
        args = self.parser.parse_args()
        objdict = storage.all()
        key = args.class_name + '.' + args.id
        if key in objdict:
            print(objdict[key])
        else:
            print("** no instance found **")

    def do_quit(self):
        """Quit command -> exit the program."""
        return True
