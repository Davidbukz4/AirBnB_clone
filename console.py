#!/usr/bin/python3
"""
Command Interpreter
"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program\n"""
        return True

    def help_EOF(self):
        print("CTRL + D (EOF) to exit the program")

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        """Doesn't execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel\n"""

    def help_create(self):
        print("Usage: create <valid class name>")

    def do_show(self, line):
        """Prints the string representation of an instance\n"""

    def help_show(self):
        print("Usage: show <valid class name> <valid id>")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id\n"""

    def help_destroy(self):
        print("Usage: destroy <valid class name> <valid id>")

    def do_all(self, line):
        """Prints all string representation of all instances\
based or not on the class name\n"""

    def help_all(self):
        print("Usage: all OR all <valid class name>")

    def do_update(self, line):
        """Updates an instance based on the class name and id by\
            adding or updating attribute\n"""

    def help_update(self):
        print("Usage: update <valid class name>", end="")
        print("<valid id> <attribute name> <attribute value>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
