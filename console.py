#!/usr/bin/python3
"""defines the console"""

import re
from shlex import split
import cmd
from models.base_model import BaseModel
import models
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter."""
    prompt = "(hbnb) "
    __classes = [
            "BaseModel", "Amenity", "State", "City", "Review", "Place", "User"
            ]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program"""
        print("")
        return True
    
    def help_quit(self):
        """Modified the documentation output"""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """Shouldn't execute anything"""
        pass

    def do_create(self, args):
        """This method Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id"""
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(f'{arg[0]}')()
            print(new_object.id)
            models.storage.save()

    def do_show(self, args):
        """Prints the string representation of an instance
            based on the class name and id"""
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f'{arg[0]}.{arg[1]}' not in models.storage.all():
            print("** no instance found **")
        else:
            obj_id = f'{arg[0]}.{arg[1]}'
            print(models.storage.all()[obj_id])

    def do_destroy(self, args):
        """Deletes an instance based on the class name
            and id (save the change into the JSON file)"""
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f'{arg[0]}.{arg[1]}' not in models.storage.all():
            print("** no instance found **")
        else:
            obj_id = f'{arg[0]}.{arg[1]}'
            del models.storage.all()[obj_id]
        models.storage.save()

    def do_all(self, args):
        """This method prints all string representation of all
            instances based or not on the class name"""
        arg = args.split()

        if len(arg) == 0:
            print([str(value) for value in models.storage.all().values()])
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in models.storage.all().items()
                  if k.startswith(arg[0])])

    def do_update(self, args):
        """This method updates an instance based on the class name
            and id by adding or updating attribute
            (save the change into the JSON file)"""
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f'{arg[0]}.{arg[1]}' not in models.storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = models.storage.all()[f'{arg[0]}.{arg[1]}']
            att_name = arg[2]
            att_value = arg[3]
            if att_value[0] == '"':
                att_value = att_value[1:-1]
            type_ = type(getattr(obj, att_name))
            setattr(obj, att_name, type_(att_value))
            models.storage.save()

        def default(self, args):
            """This is the default behavior for
                cmd module when input is invalid"""
            arg = args.split('.')

            if arg[0] in self.__classes:
                if arg[1] == 'all()':
                    self.do_all(arg[0])
                elif arg[1] == 'count()':
                    lst = [str(v) for k, v in models.storage.all().items()
                           if k.startswith(arg[0])]
                    print(len(lst))
                elif arg[1].startswith("show"):
                    i_d = arg[1].split('"')[1]
                elif arg[1].startswith('show'):
                    i_d = arg[1].split('"')
                    obj_id = f'{arg[0]}.{i_d[1]}'
                    if obj_id not in models.storage.all():
                        print('** no instance found **')
                    else:
                        print(models.storage.all()[obj_id])
                elif arg[1].startswith('destroy'):
                    i_d = arg[1].split('"')
                    obj_id = f"{arg[0]}.{i_d[1]}"
                    if obj_id not in models.storage.all():
                        print('** no instance found **')
                    else:
                        del models.storage.all()[obj_id]
                    models.storage.save()
                elif arg[1].startswith('update'):
                    att = arg[1].split('"')
                    obj_id = f"{arg[0]}.{att[1]}"
                    print(arg[1][47:-1])
                    if obj_id not in models.storage.all():
                        print('** no instance found**')
                    elif not (att[2].startswith(', {')):
                        att_id = att[1]
                        att_name = att[3]
                        att_value = att[5]
                        lst = f'{arg[0]} {att_id} {att_name} {att_value}'
                        self.do_update(lst)
                    else:
                        att_dict = eval(arg[1][47:-1])
                        obj = models.storage.all()[obj_id]
                        for k, v in att_dict.items():
                            type_ = type(getattr(obj, k))
                            setattr(obj, k, type_(v))
                            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
