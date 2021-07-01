#!/usr/bin/python3
"""Command interpreter Module"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """ exit the console """
        return True

    def emptyline(self):
        """ emptyline method """
        pass

    def do_quit(self, line):
        """ quit cmd to exit the program """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
