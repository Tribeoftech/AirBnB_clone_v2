#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


def checkInt(s, neg):
    '''Checks if string is an integer'''
    if neg == 1 and s.startswith('-'):
        if s[1:].isnumeric():
            return True, s
    elif s.isnumeric():
        return True
    return False


def escQuotes(s):
    '''Checks escapes quotes'''
    for i, char in enumerate(s):
        if char == '"':
            if s[i - 1] != '\\':
                return False
    return True


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int
    }

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        print()
        sys.exit()

    def do_EOF(self, arg):
        '''Handles EOF (Ctrl+D)'''
        return True

    def do_create(self, arg):
        '''Create command to create a new instance'''
        if not arg:
            print('** class name missing **')
        elif arg not in self.classes:
            print('** class doesn\'t exist **')
        else:
            newInstance = self.classes[arg]()
            newInstance.save()
            print(newInstance.id)

    def do_show(self, arg):
        '''Show command to display an instance'''
        args = arg.split()
        if not arg:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            instances = storage.all()
            key = args[0] + '.' + args[1]
            if key in instances:
                print(instances[key])
            else:
                print('** no instance found **')

    def do_destroy(self, arg):
        '''Destroy command to delete an instance'''
        args = arg.split()
        if not arg:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            instances = storage.all()
            key = args[0] + '.' + args[1]
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, arg):
        '''All command to display all instances or all instances of a class'''
        args = arg.split()
        instances = storage.all()
        if not arg:
            print([str(value) for value in instances.values()])
        elif args[0] not in self.classes:
            print('** class doesn\'
