#!/usr/bin/python3
"""Point of entry of the CLI
(cmd line interpreter)"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

lists = ['BaseModel', 'User', 'Place','State', 
         'City','Amenity', 'Review']


class HBNBCommand(cmd.Cmd):
    """CL Interpreter"""
    prompt = '(hbnb) '

    def help_quit(self):
        print('Quit command to exit the program\n')

    def emptyline(self):
        """shouldn’t execute anything
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """End-of-file
        """
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        ex: create BaseModel
        """
        """lists = ['BaseModel', 'User']"""
        if not arg:
            print('** class name missing **')
        elif arg not in lists:
            print('** class doesn\'t exist **')

        else:                   
            if arg == 'BaseModel':
                arg = BaseModel()
            elif arg == 'User':
                arg = User()
            elif arg == 'Place':
                arg = Place()
            elif arg == 'State':
                arg = State()
            elif arg == 'City':
                arg = City()
            elif arg == 'Amenity':
                arg = Amenity()
            elif arg == 'Review':
                arg = Review()

            arg.save()
            print(arg.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        ex: show BaseModel 1234-1234-1234
        """
        swargs = arg.split()
        """lists = ['BaseModel', 'User']"""

        if len(swargs) == 0:
            print('** class name missing **')

        elif swargs[0] not in lists:
            print('** class doesn\'t exist **')

        elif len(swargs) == 1:
            print('** instance id missing **')

        elif len(swargs) == 2:
            dicts = storage.all()

            """obj_key = v.__class__.__name__ + '.' + v.id"""

            add_swargs = swargs[0] + '.' + swargs[1]

            for k, v in dicts.items():
                obj_key = v.__class__.__name__ + '.' + v.id

                if (add_swargs == obj_key):
                    print(dicts[add_swargs])
                    return

            print('** no instance found **')

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        ex: destroy BaseModel 1234-1234-1234
        """
        swargs = arg.split()
        """lists = ['BaseModel', 'User']"""

        if len(swargs) == 0:
            print('** class name missing **')

        elif swargs[0] not in lists:
            print('** class doesn\'t exist **')

        elif len(swargs) == 1:
            print('** instance id missing **')

        elif len(swargs) == 2:
            dicts = storage.all()

            add_swargs = swargs[0] + '.' + swargs[1]

            for k, v in dicts.items():
                obj_key = v.__class__.__name__ + '.' + v.id

                if (add_swargs == obj_key):
                    del (dicts[add_swargs])
                    storage.save()
                    return

            print('** no instance found **')

    def do_all(self, arg):
        """prints all string representation of all
        instances based or not on the class name
        ex: all BaseModel or all
        """
        open_b = '["'
        close_b = '"]'
        """lists = ['BaseModel', 'User']"""

        if len(arg) == 0 or arg in lists:
            print(open_b, end="")

            dicts = storage.all()

            for k, v in dicts.items():
                obj_key = v.__class__.__name__ + '.' + v.id
                print(dicts[obj_key], end="")
            print(close_b)

        elif arg not in lists:
            print('** class doesn\'t exist **')

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        Ex: $ update BaseModel 1234-1234-1234
        email "aibnb@mail.com"
        All other arguments should not be used
        Ex: $ update BaseModel 1234-1234-1234 email
        "aibnb@mail.com" first_name "Betty" =
        update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        swargs = arg.split()
        """add_swargs = swargs[0] + '.' + swargs[1]"""
        dicts = storage.all()
        """lists = ['BaseModel', 'User']"""

        if len(swargs) == 0:
            print('** class name missing **')

        elif swargs[0] not in lists:
            print('** class doesn\'t exist **')

        elif len(swargs) == 1:
            print('** instance id missing **')

        else:
            add_swargs = swargs[0] + '.' + swargs[1]

            if add_swargs not in dicts:
                print('** no instance found **')

            elif len(swargs) == 2:
                print('** attribute name missing **')

            elif len(swargs) == 3:
                print('** value missing **')

            else:
                attri = swargs[2]
                val = swargs[3].strip('"\'')
                obj = dicts[add_swargs]

                obj.__dict__[attri] = val
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
