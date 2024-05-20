#!/usr/bin/python3
"""
This module contains entry point of command interpreter
"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


_classes = {"BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity,
            "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class is entry point of the command interpreter """

    prompt = '(hbnb) '
    classes = ["BaseModel", "User", "State", "City",
               "Amenity",
               "Place",
               "Review"]

    def emptyline(self):
        """Don't Execute anything on empty line\n"""
        pass

    def do_quit(self, args):
        """Quit cmd exit the program.\n"""
        quit()

    def do_EOF(self, args):
        """End Of File cmd exit the program"""
        quit()

    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        args = shlex.split(args)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in _classes:
            print("** class doesn't exist **")
            return

        if args[0] in _classes:
            new_object = eval(args[0])()
            new_object.save()
            print(new_object.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """

        args_list = shlex.split(args)

        if not args:
            print("** class name missing **")
            return

        elif args_list[0] not in _classes:
            print("** class doesn't exist **")
            return

        elif len(args_list) == 1:
            print("** instance id missing **")
            return

        new_object = "{}.{}".format(args_list[0], args_list[1])

        if new_object not in models.storage.all().keys():

            print("** no instance found **")
            return

        else:
            print("[{}] ({}) {}".format(args_list[0], new_object[1],
                  models.storage.all()[new_object]))

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234"""

        args_list = shlex.split(args)

        if len(args_list) == 0:
            print("** class name missing **")
            return
        elif args_list[0] in _classes:

            if len(args_list) > 1:

                key = args_list[0] + "." + args_list[1]

                if key in models.storage.all():
                    del models.storage.all()[key]

                    models.storage.save()

                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all"""

        new_object = models.storage.all()
        list_objects = []

        if args not in _classes:
            print("** class doesn't exist **")
            return
        if args in self.classes:
            for key, value in new_object.items():
                if args in key:

                    toke_key = key.split(".")

                    key_new = "[" + toke_key[0] + "]"\
                        + " (" + toke_key[1] + ")"
                    list_objects.append(key_new + " " + str(value))
                    print(list_objects)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)."""

        if args == '':
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        key = args_list[0] + "." + args_list[1]
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args_list) == 2:
            print("** attribute name missing **")
            return
        if len(args_list) == 3:
            print("** value missing **")
            return
        attribute = args_list[2]
        value = args_list[3]
        if '"' in value:
            value = value.strip('"')

        try:
            setattr(all_objects[key], attribute, value)
            models.storage.save()
        except AttributeError:
            print("** attr name missing **")
            return

    def do_count(self, args):
        """retrieve the number of instances of a class: <class name>.count()"""
        counter = 0
        _objects = models.storage.all()

        if args in self.classes:
            for key in _objects.keys():
                find_class = key.split(".")

                if find_class[0] == args:
                    counter += 1
            print(counter)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
