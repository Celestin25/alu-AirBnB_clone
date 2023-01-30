import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True
    
    def emptyline(self):
        """Do not execute anything on an empty line"""
        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
