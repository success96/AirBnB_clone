#!/usr/bin/python3
'''defines the console'''


import cmd
from models.base_model  import BaseModel
import models
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place

class HBNBCommand(cmd.Cmd):

    """Class for command interpreter."""

    prompt = "(hbnb) "
    __classes = ["BaseModel", "Amenity", "State", "City", "Review", "Place"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program"""
        return True

    def emptyline(self):
        return
    
    def do_create(self, args):
        """
        This method Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id
        """
        arg = args.split( )

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_object = eval (f'{arg[0]}')()
            print(new_object.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance 
        based on the class name and id
        """
        arg = args.split()

        if len(arg) == 0:
            print ("** class name missing **")
        elif arg[0] not in self.__classes:
            print ("** class doesn't exist **")
        elif len(arg) == 1:
            print ("** instance id missing **")
        elif f'{arg[0]}.{arg[1]}' not in models.storage.all():
            print("** no instance found **")
        else:
            obj_id = f'{arg[0]}.{arg[1]}'
            print(models.storage.all()[obj_id])

    def do_destroy(self, args):
            """
            Deletes an instance based on the class name 
            and id (save the change into the JSON file)
            """
            arg = args.split()

            if len(arg) ==0:
                print ("** class name missing **")
            elif arg[0] not in self.__classes:
                print ("** class doesn't exist **")
            elif len(arg) == 1:
                print ("** instance id missing **")
            elif f'{arg[0]}.{arg[1]}' not in models.storage.all():
                print("** no instance found **")
            else:
                obj_id = f'{arg[0]}.{arg[1]}'
                del models.storage.all()[obj_id]
            models.storage.save()
  
    def do_all(self, args):
        """
        This method prints all string representation of all 
        instances based or not on the class name
        """
        arg = args.split()

        if len(arg) ==0:
            print([str(value) for value in models.storage.all().values()])
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **") 
        else:
            print([str(v) for k, v in models.storage.all().items() if k.startswith(arg[0])])

    def do_update(self, args):
        """
        This method updates an instance based on the class name 
        and id by adding or updating attribute 
        (save the change into the JSON file)
        """
        arg = args.split()
        if len(arg) ==0:
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
            att = arg[2]
            obj.__dict__[att] = type(obj.__dict__[att])(arg[3])
            print(obj.__dict__)
            obj.save()




if __name__ == '__main__':
    HBNBCommand().cmdloop()
