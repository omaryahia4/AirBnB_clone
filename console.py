#!/usr/bin/python3
"""Command interpreter Module"""

import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class """
    prompt = "(hbnb)"
    Classes = [
        "BaseModel", "User", "State",
        "Place", "City", "Amenity",
        "Review"
        ]

    def do_EOF(self, line):
        """ exit the console """
        return True

    def emptyline(self):
        """ emptyline method """
        pass

    def do_quit(self, line):
        """ quit cmd to exit the program """
        return True

    def do_create(self, arg):
        """Dynamically created a class"""
        arg = arg.split(" ")
        if arg == '':
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.Classes:
            print("** class doesn't exist **")
            return
        else:
            obj = eval(arg)()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """String representation of an instance
         based on the class name and id"""
        arg = args.split(" ")
        if arg == "":
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.Classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        else:
            objects = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            try:
                obj = objects[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based
         on the class name and id"""
        arg = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id is missing **")
            return
        key = arg[0] + "." + arg[1]
        objects_dict = storage.all()
        if key in objects_dict:
            del objects_dict[key]
            storage.save()
            print(storage.all())

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        arg = arg.split()
        objects_dict = storage.all()
        List = []
        if len(arg):
            class_name = arg[0]
            if class_name not in HBNBCommand.Classes:
                print("** class doesn't exist **")
                return
            for key, value in objects_dict.items():
                if class_name in key:
                    List.append((objects_dict[key].__str__()))
        else:
            for key, value in objects_dict.items():
                List.append((objects_dict[key].__str__()))
        print(List)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        and saves the change into the JSON file
        """
        if arg == '':
            print("** class name missing **")
            return
        arg = arg.split()
        if arg[0] not in HBNBCommand.Classes:
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        key = arg[0] + "." + arg[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        val = arg.split('"')
        if len(val) == 1:
            print("** value missing **")
            return
        attr = arg[2]
        try:
            value = getattr(objects[key], attr)
            t = type(value)
            setattr(objects[key], attr, t(val[1]))
        except:
            setattr(objects[key], attr, val[1])
        storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
