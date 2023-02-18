#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
         "BaseModel",
         "User",
         "State",
         "City",
         "Place",
         "Amenity",
         "Review"
    }

    def emptyline(self):
        """Shouldn’t execute anything"""
        pass

    def default(self, arg):
        """Default behaviour"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        match = re.search(r"\.", arg)
        if match is not None:
            clin = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", clin[1])
            if match is not None:
                command = [clin[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(clin[0], command[1])
                    return argdict[command[0]](call)
        print("** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Should exit the program"""
        print("")
        return True

    def help_quit(self):
        """Modified the documentation output"""
        print("Quit command to exit the program\n")

    def do_create(self, arg):
        """Usage: Create <class>
        Create a new class instance and prints its id
        """
        clin = parse(arg)
        if len(clin) == 0:
            print("** class name missing **")
        elif clin[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(clin[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        clin = parse(arg)
        objectDict = storage.all()
        if len(clin) == 0:
            print("** class name missing **")
        elif clin[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(clin) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(clin[0], clin[1]) not in objectDict:
            print("** no instance found **")
        else:
            print(objectDict["{}.{}".format(clin[0], clin[1])])

    def do_destroy(self, arg):
        """Usage: Destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id"""
        clin = parse(arg)
        objectDict = storage.all()
        if len(clin) == 0:
            print("** class name missing **")
        elif clin[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(clin) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(clin[0], clin[1]) not in objectDict.keys():
            print("** no instance found **")
        else:
            del objectDict["{}.{}".format(clin[0], clin[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        clin = parse(arg)
        if len(clin) > 0 and clin[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(clin) > 0 and clin[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(clin) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        clin = parse(arg)
        objectDict = storage.all()

        if len(clin) == 0:
            print("** class name missing **")
            return False
        if clin[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(clin) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(clin[0], clin[1]) not in objectDict.keys():
            print("** no instance found **")
            return False
        if len(clin) == 2:
            print("** attribute name missing **")
            return False
        if len(clin) == 3:
            try:
                type(eval(clin[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(clin) == 4:
            obj = objectDict["{}.{}".format(clin[0], clin[1])]
            if clin[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[clin[2]])
                obj.__dict__[clin[2]] = valtype(clin[3])
            else:
                obj.__dict__[clin[2]] = clin[3]
        elif type(eval(clin[2])) == dict:
            obj = objectDict["{}.{}".format(clin[0], clin[1])]
            for k, v in eval(clin[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class"""
        clin = parse(arg)
        count = 0
        for obj in storage.all().values():
            if clin[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
