class HBNBCommand(cmd.Cmd):
    def parse_input(self, arg):
        curly_braces = re.search(r"\{(.*?)\}", arg)
        brackets = re.search(r"\[(.*?)\]", arg)
        if curly_braces is None:
            if brackets is None:
                return [i.strip(",") for i in arg.split()]
            else:
                lexer = arg[:brackets.span()[0]].split()
                retl = [i.strip(",") for i in lexer]
                retl.append(brackets.group())
                return retl
        else:
            lexer = arg[:curly_braces.span()[0]].split()
            retl = [i.strip(",") for i in lexer]
            retl.append(curly_braces.group())
            return retl

    def emptyline(self):
        pass

    def default(self, arg):
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print("")
        return True

    def do_create(self, args):
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in self.__all_classes:
            print("** class doesn't exist **")
            return
        new_object = eval(class_name + "()")
        new_object.save()
        print(new_object.id)
        storage.save()

    def do_show(self, args):
        arg_list = self.parse_input(args)
        objdict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        elif arg_list[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        elif len(arg_list) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(arg_list[0], arg_list[1
