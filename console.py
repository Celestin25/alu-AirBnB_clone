import cmd

class HBNBCommand(cmd.Cmd):
    """
    Class that implements the command line interpreter for the AirBnB clone
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True
    
    def do_EOF(self, line):
        """
        Exits the program
        """
        return True

    def emptyline(self):
        """
        Override the default behavior of cmd when an empty line is entered
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
