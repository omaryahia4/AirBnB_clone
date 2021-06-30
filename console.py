#!/usr/bin/python3
"""Command interpreter Module"""

import cmd


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
