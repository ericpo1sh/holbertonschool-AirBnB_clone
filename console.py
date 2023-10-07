#!/usr/bin/python3
""" module contains console for command interpreter """
import cmd
import shlex
from models import storage
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    """ Initializing infinite loop and prompt to display """
    prompt = '(hbnb) '
    class_list = [
        "BaseModel",
        # "Amenity": Amenity(),
        # "City": City(),
        # "Place": Place(),
        # "Review": Review()
        # "State": State(),
        # "User": User(),
    ]

    def emptyline(self):
        """ If line is empty, do nothing. """
        pass

    def do_EOF(self, *line):
        """ Quits upon receiving EOF as input. """
        print()
        return True

    def do_quit(self, *line):
        """ Quit command to exit the program. """
        return True

    def do_create(self, line):
        """ Creates a new instance of BaseModel and saves to JSON. """
        if not line:
            print('** class name missing **')
            return
        class_name = line.split()[0]
        if class_name not in self.class_list:
            print('** class doesn\'t exist **')
            return
        object = eval(class_name)()
        object.save()
        print(object.id)

    def do_show(self, line):
        """ Prints string representation of instance based on class name. """
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        if args[0] not in self.class_list:
            print('** class doesn\'t exist **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        obj_dict = storage.all()
        obj_key = f'{args[0]}.{args[1]}'
        if obj_key not in obj_dict:
            print('** no instance found **')
            return
        print(obj_dict[obj_key])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id. """
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        if args[0] not in self.class_list:
            print('** class doesn\'t exist **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        obj_dict = storage.all()
        obj_key = f'{args[0]}.{args[1]}'
        if obj_key not in obj_dict:
            print('** no instance found **')
            return
        del obj_dict[obj_key]
        storage.save()

    def do_all(self, line):
        """ Prints string representation of all instances based on class. """
        args = line.split()
        if args:
            if args[0] not in self.class_list:
                print('** class doesn\'t exist **')
                return
            obj_dict = storage.all()
            obj_list = []
            for key, value in obj_dict.items():
                if key.split(".")[0] == args[0]:
                    obj_list.append(value)
        else:
            obj_list = storage.all().values()
        for obj in obj_list:
            print(str(obj))

    def do_update(self, line):
        """ Updates an instance based class name, id by adding an attribute """
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        if args[0] not in self.class_list:
            print('** class doesn\'t exist **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        obj_dict = storage.all()
        obj_key = f'{args[0]}.{args[1]}'
        objs = obj_dict.get(obj_key)
        if obj_key not in obj_dict:
            print('** no instance found **')
            return
        if len(args) < 3:
            print('** attribute name missing **')
            return
        if len(args) < 4:
            print('** value missing **')
            return
        setattr(objs, args[2], args[3].replace('"', ''))
        objs.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
