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
        line = line.split(' ')
        if line[0]:
            if line[0] == 'BaseModel':
                inst = eval(line[0] + '()')
                models.storage.save()
                print(inst.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        print("Usage: create <valid class name>")

    def do_show(self, line):
        """Prints the string representation of an instance\n"""
        line = line.split(' ')
        if len(line) == 2:
            if line[0] == 'BaseModel':
                objs = models.storage.all()
                obj_dic = []
                for key, value in objs.items():
                    key_obj = key.split('.')[1]
                    if key_obj == line[1]:
                        obj_dic.append(objs[key])
                if obj_dic:
                    for x in obj_dic:
                        print(x)
                    return
                print('** no instance found **')
        elif len(line) == 1 and line[0]:
            if line[0] == 'BaseModel':
                print('** instance id missing **')
                return
            print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def help_show(self):
        print("Usage: show <valid class name> <valid id>")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id\n"""
        line = line.split(' ')
        if len(line) == 2:
            if line[0] == 'BaseModel':
                key = '{}.{}'.format(line[0], line[1])
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                    return
                print('** no instance found **')
        elif len(line) == 1 and line[0]:
            if line[0] == 'BaseModel':
                print('** instance id missing **')
                return
            print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def help_destroy(self):
        print("Usage: destroy <valid class name> <valid id>")

    def do_all(self, line):
        """Prints all string representation of all instances\
           based or not on the class name\n"""
        line = line.split(' ')
        objs = models.storage.all()
        if len(line) == 1 and line[0]:
            if line[0] == 'BaseModel':
                for key in objs:
                    if key.split('.')[0] == line[0]:
                        print(objs[key])
            else:
                print("** class doesn't exist **")
        else:
            for key in objs:
                print(objs[key])

    def help_all(self):
        print("Usage: all OR all <valid class name>")

    def do_update(self, line):
        """Updates an instance based on the class name and id by\
           adding or updating attribute\n"""
        line = line.split(' ')
        if line and line[0]:
            if line[0] == 'BaseModel':
                if len(line) == 1:
                    print('** instance id missing **')
                    return
                key = '{}.{}'.format(line[0], line[1])
                if key in models.storage.all():
                    obj = models.storage.all()[key]
                    if len(line) == 2:
                        print('** attribute name missing **')
                        return
                    elif len(line) == 3:
                        print('** value missing **')
                        return
                    if line[2] in type(obj).__dict__:
                        value_type = type(obj.__class__.__dict__[line[2]])
                        setattr(obj, line[2], value_type(line[3]))
                    else:
                        setattr(obj, line[2], line[3])
                    models.storage.save()
                else:
                    print('** no instance found **')
                    return
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def help_update(self):
        print("Usage: update <valid class name>", end="")
        print("<valid id> <attribute name> <attribute value>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
