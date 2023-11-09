#!/usr/bin/python3
'''defines the console'''
import cmd
from models.base_model  import BaseModel

class HBNBCommand(cmd.Cmd):

    """Class for command interpreter."""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program
        """
        return True

    def emptyline(self):
        return
    
    def do_create(self, line):
        args = arg.split()

        if len(line) ==0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_object = eval (f'{args[0]}')()
            print(new_object.id)

    def do_show(self, line):
        args = arg.split()

        if len(args) ==0:
            print ("** class name missing **")
        elif args[0] not in self.__classes:
            print ("** class doesn't exist **")
        elif len(args) == 1:
            print ("** instance id missing **")
        elif f'(args[0]] [1]]' not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f'args[0]).[args[1]]'])


  def do_destroy(self, line):
        args = arg.split()

        if len(args) ==0:
            print ("** class name missing **")
        elif args[0] not in self.__classes:
            print ("** class doesn't exist **")
        elif len(args) == 1:
            print "** instance id missing **")
        elif f'(args[0]] [1]]' not in storage.all():
            print("** no instance found **")
        else:
            del storage.all() [f' (args [0]] [args[1]]']
        storage.save()
  
  def do_all(self, line):
      args = arg.split()

      if len(args) ==0:
          print([str(value) for value in storage.all().values()])
      elif args[0] not in self.__classes:
          print("** class doesn't exist **") 
      else:
          print([str(v) for k, v in storage.all().items() if k.startswith([args[0])])

  def do_update:
  args = arg.split()
      if len(args) ==0:
          print("** class name missing **")
      elif args[0] not in self.__classes:
          print("** class doesn't exist **")
      elif len(args) == 1:
          print("** instance id missing **")
      elif f'[args[0]] [args[1]]' not in storage.all():
          print("** no instance found **")
      elif len(args) == 2:
          print("** attribute name missing **")
      elif len(args) == 3:
          print("** value missing **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
