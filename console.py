#!/usr/bin/python3
""" module contains console for command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Initializing infinite loop and prompt to display """
    prompt = '(hbnb) '

    def emptyline(self):
        """ If line is empty, do nothing """
        pass

    def do_EOF(self, *line):
        """ Quits upon receiving EOF as input """
        print()
        return True

    def do_quit(self, *line):
        """ Quit command to exit the program """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
